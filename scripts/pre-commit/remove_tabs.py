from pathlib import Path
import sys

changed_files = []

for filename in sys.argv[1:]:
    path = Path(filename)

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue

    fixed = text.replace("\t", "    ")

    if fixed != text:
        path.write_text(fixed, encoding="utf-8")
        changed_files.append(filename)

if changed_files:
    print("🚀 Replaced tabs with spaces in:")
    for filename in changed_files:
        print(f"  - {filename}")
    raise SystemExit(1)

raise SystemExit(0)
