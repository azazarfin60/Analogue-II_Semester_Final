import os
import glob

def check_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    errors = []
    in_math_block = False
    
    for i, line in enumerate(lines):
        line = line.strip('\n')
        if line.strip() == '$$':
            if not in_math_block:
                # Starting a math block
                in_math_block = True
                # Check previous line
                if i > 0 and lines[i-1].strip() != '':
                    errors.append(f"Line {i+1}: Missing blank line BEFORE starting $$ block")
            else:
                # Ending a math block
                in_math_block = False
                # Check next line
                if i < len(lines) - 1 and lines[i+1].strip() != '':
                    errors.append(f"Line {i+1}: Missing blank line AFTER ending $$ block")

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
    print("All good! No $$ block formatting errors found.")
else:
    print(f"Total errors found: {total_errors}")

