import os
import re
import sys
import json
import subprocess
import argparse

def sanitize_filename(title):
    # Remove characters that are illegal or problematic in filenames
    sanitized = re.sub(r'[\\/*?:"<>|]', "", title)
    # Replace multiple spaces with a single space
    sanitized = re.sub(r'\s+', " ", sanitized)
    return sanitized.strip()

def format_timestamp(seconds):
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"[{minutes:02d}:{secs:02d}]"

def download_audio(video_id, temp_dir):
    os.makedirs(temp_dir, exist_ok=True)
    audio_path_template = os.path.join(temp_dir, f"{video_id}.%(ext)s")
    audio_path = os.path.join(temp_dir, f"{video_id}.mp3")
    
    # Clean up existing audio if present
    if os.path.exists(audio_path):
        try:
            os.remove(audio_path)
        except Exception:
            pass

    print(f"  --> Downloading audio for video {video_id} using yt-dlp...")
    cmd = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "-f", "bestaudio",
        "-o", audio_path_template,
        f"https://www.youtube.com/watch?v={video_id}"
    ]
    
    # Run yt-dlp and hide stdout to keep console clean unless error occurs
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  --> yt-dlp download failed with return code {result.returncode}")
        print(result.stderr)
        raise RuntimeError(f"Failed to download audio for {video_id}")
    
    if not os.path.exists(audio_path):
        # In case the extension resolved differently, let's search for the file
        files = [f for f in os.listdir(temp_dir) if f.startswith(video_id)]
        if files:
            audio_path = os.path.join(temp_dir, files[0])
        else:
            raise FileNotFoundError(f"Could not locate downloaded audio file for {video_id}")
            
    return audio_path

def main():
    parser = argparse.ArgumentParser(description="Download and transcribe transcripts for a YouTube playlist.")
    parser.add_argument("--playlist", type=str, 
                        default="https://www.youtube.com/playlist?list=PLs5_Rtf2P2r5MplAOADz3fTWIyBZTkGbB", 
                        help="YouTube playlist URL")
    parser.add_argument("--output-dir", type=str, 
                        default="Ankit_Goyal_sir_analog", 
                        help="Output directory for transcripts")
    parser.add_argument("--whisper-model", type=str, 
                        default="small", 
                        help="Whisper model size to use for local transcription (tiny, base, small, medium, large)")
    parser.add_argument("--use-faster-whisper", type=bool, 
                        default=True, 
                        help="Use faster-whisper (faster/less memory) instead of standard whisper")
    parser.add_argument("--force-local", type=bool, 
                        default=True, 
                        help="Bypass YouTube transcript download and use local GPU transcription directly")
    args = parser.parse_args()

    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)
    temp_dir = "temp_audio"
    
    print(f"Fetching playlist entries from: {args.playlist}")
    cmd = ["yt-dlp", "--flat-playlist", "--dump-single-json", args.playlist]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error fetching playlist metadata.")
        print(result.stderr)
        sys.exit(1)
        
    try:
        playlist_data = json.loads(result.stdout)
    except Exception as e:
        print(f"Failed to parse playlist JSON: {e}")
        sys.exit(1)
        
    entries = playlist_data.get("entries", [])
    total_videos = len(entries)
    print(f"Found {total_videos} videos in playlist: '{playlist_data.get('title', 'Unknown')}'")
    
    # Initialize GPU configuration
    import torch
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"CUDA status for local transcription: PyTorch CUDA available = {torch.cuda.is_available()} (Device: {device})")
    
    whisper_model = None
    
    for i, entry in enumerate(entries, 1):
        if not entry:
            continue
        video_id = entry.get("id")
        video_title = entry.get("title")
        if not video_id or not video_title:
            continue
            
        sanitized_title = sanitize_filename(video_title)
        filename = f"{i:03d}_{sanitized_title}.txt"
        file_path = os.path.join(output_dir, filename)
        
        # Check if already processed
        if os.path.exists(file_path):
            print(f"[{i}/{total_videos}] Skipping '{video_title}' - transcript already exists.")
            continue
            
        print(f"\n[{i}/{total_videos}] Processing '{video_title}' ({video_id})...")
        
        transcript_text = None
        
        # Try downloading transcript from YouTube if not forced local
        if not args.force_local:
            try:
                from youtube_transcript_api import YouTubeTranscriptApi
                from deep_translator import GoogleTranslator
                
                print("  --> Attempting to fetch transcript from YouTube...")
                transcript_list = YouTubeTranscriptApi().list(video_id)
                
                # Check for English or Hindi transcripts
                try:
                    t_en = transcript_list.find_transcript(['en', 'en-US'])
                    print("  --> Found English transcript directly on YouTube.")
                    fetched = t_en.fetch()
                    lines = [f"{format_timestamp(e['start'])} {e['text'].replace('\n', ' ')}" for e in fetched]
                    transcript_text = "\n".join(lines)
                except Exception:
                    # English not found, try Hindi and translate
                    t_hi = transcript_list.find_transcript(['hi'])
                    print("  --> Found Hindi transcript. Downloading and translating to English...")
                    fetched = t_hi.fetch()
                    
                    # Prepare texts to translate
                    texts = [e['text'].replace('\n', ' ').strip() for e in fetched]
                    timestamps = [format_timestamp(e['start']) for e in fetched]
                    
                    # Group translation requests to speed up and prevent 429
                    translator = GoogleTranslator(source='hi', target='en')
                    translated_texts = []
                    
                    chunk = []
                    chunk_len = 0
                    for text in texts:
                        if chunk_len + len(text) + 1 > 4500:
                            joined_chunk = "\n".join(chunk)
                            res = [s.strip() for s in translator.translate(joined_chunk).split("\n")]
                            if len(res) == len(chunk):
                                translated_texts.extend(res)
                            else:
                                # Fallback line-by-line for this chunk
                                translated_texts.extend([translator.translate(t) if t else "" for t in chunk])
                            chunk = []
                            chunk_len = 0
                        chunk.append(text)
                        chunk_len += len(text) + 1
                    
                    if chunk:
                        joined_chunk = "\n".join(chunk)
                        res = [s.strip() for s in translator.translate(joined_chunk).split("\n")]
                        if len(res) == len(chunk):
                            translated_texts.extend(res)
                        else:
                            translated_texts.extend([translator.translate(t) if t else "" for t in chunk])
                            
                    lines = [f"{ts} {txt}" for ts, txt in zip(timestamps, translated_texts)]
                    transcript_text = "\n".join(lines)
            except Exception as e:
                print(f"  --> YouTube transcript lookup/translation failed: {e}")
                
        # If no transcript downloaded (or forced local), download audio and transcribe
        if not transcript_text:
            print("  --> Using local GPU translation...")
            try:
                audio_path = download_audio(video_id, temp_dir)
                
                # Load model lazily
                if whisper_model is None:
                    if args.use_faster_whisper:
                        from faster_whisper import WhisperModel
                        print(f"  --> Loading faster-whisper model '{args.whisper_model}' on {device}...")
                        compute_type = "float16" if device == "cuda" else "int8"
                        whisper_model = WhisperModel(args.whisper_model, device=device, compute_type=compute_type)
                    else:
                        import whisper
                        print(f"  --> Loading standard Whisper model '{args.whisper_model}' on {device}...")
                        whisper_model = whisper.load_model(args.whisper_model, device=device)
                
                print("  --> Transcribing and translating audio...")
                lines = []
                if args.use_faster_whisper:
                    segments, info = whisper_model.transcribe(audio_path, task="translate")
                    print(f"  --> Audio detected as {info.language} (probability: {info.language_probability:.2f})")
                    for segment in segments:
                        timestamp = format_timestamp(segment.start)
                        text = segment.text.strip()
                        lines.append(f"{timestamp} {text}")
                        # Print status line
                        print(f"\r      [{timestamp}] {text[:60]}...", end="", flush=True)
                    print()
                else:
                    whisper_result = whisper_model.transcribe(audio_path, task="translate")
                    for segment in whisper_result.get("segments", []):
                        timestamp = format_timestamp(segment["start"])
                        text = segment["text"].strip()
                        lines.append(f"{timestamp} {text}")
                
                transcript_text = "\n".join(lines)
                
                # Clean up temporary audio file
                if os.path.exists(audio_path):
                    os.remove(audio_path)
                    
            except Exception as ex:
                print(f"  --> Failed to transcribe '{video_title}' locally: {str(ex)}")
                
        if transcript_text:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"Title: {video_title}\n")
                f.write(f"URL: https://www.youtube.com/watch?v={video_id}\n")
                source_info = f"Local Whisper ({args.whisper_model})" if not args.force_local and not transcript_text else "Local Whisper (GPU Translation)"
                f.write(f"Source: {source_info}\n\n")
                f.write(transcript_text)
            print(f"  --> Successfully saved transcript to: {file_path}")
        else:
            print(f"  --> [ERROR] Could not generate transcript for '{video_title}'")

    # Clean up temp directory
    if os.path.exists(temp_dir):
        try:
            for f in os.listdir(temp_dir):
                os.remove(os.path.join(temp_dir, f))
            os.rmdir(temp_dir)
        except Exception:
            pass

    print("\nProcessing complete! All transcripts are stored in:", output_dir)

if __name__ == "__main__":
    main()
