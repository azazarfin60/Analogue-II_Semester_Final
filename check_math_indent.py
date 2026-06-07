import os
import glob

def check_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    errors = []
    in_math_block = False
    
    for i, line in enumerate(lines):
        line = line.rstrip('\n')
        if line.strip() == '$$':
            in_math_block = not in_math_block
            continue
            
        if in_math_block:
            if line.startswith('    ') or line.startswith('\t'):
                errors.append(f"Line {i+1}: Math inner content is indented by 4+ spaces or tab")

    return errors

d = '/home/azaz/AntigravityData/Analogue-II_Semester_Final/boss_notes_updated'
files = glob.glob(os.path.join(d, '*.md'))

total_errors = 0
for f in sorted(files):
    errs = check_file(f)
    if errs:
        print(f"File: {os.path.basename(f)}")
        for e in errs:
            print("  -", e)
        total_errors += len(errs)

if total_errors == 0:
    print("All good! No inner math indent errors found.")
else:
    print(f"Total errors found: {total_errors}")

