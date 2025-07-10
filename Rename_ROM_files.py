import os
import re
from pathlib import Path
from difflib import get_close_matches

# Set your folder paths
folder_a = Path(r"D:\Roms_test\GBA")
folder_b = Path(r"D:\Roms_test\Completed Covers")
unmatched_output_dir = Path(r"D:\Roms_test\unamed")
unmatched_output_dir.mkdir(parents=True, exist_ok=True)
unmatched_file_path = unmatched_output_dir / "unmatched_files.txt"

CLEANUP_WORDS = [
    "version", "usa", "europe", "rev", "gamecoverdocument",
    "(", ")", "-", "_"
]

def clean_name(name: str) -> str:
    name = name.lower()
    for word in CLEANUP_WORDS:
        name = name.replace(word, "")
    name = re.sub(r'[^a-z0-9 ]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name

# Prepare cleaned map of Folder B
folder_b_files = list(folder_b.glob("*"))
cleaned_b = {
    clean_name(f.stem): f for f in folder_b_files
}

rename_plan = []
unmatched_files = []

# Scan files with progress output
print("\n🔍 Scanning files in Folder A...\n")
for idx, file_a in enumerate(folder_a.iterdir(), start=1):
    if not file_a.is_file():
        continue

    print(f"📄 [{idx}] Processing: {file_a.name}")

    match = re.match(r"\s*\d+\s*(.+)", file_a.stem, re.IGNORECASE)
    if not match:
        unmatched_files.append(f"{file_a.name} (bad format)")
        continue

    base_clean = clean_name(match.group(1))
    match_list = get_close_matches(base_clean, cleaned_b.keys(), n=1, cutoff=0.4)

    if match_list:
        best_key = match_list[0]
        matched_file = cleaned_b[best_key]
        new_name = file_a.stem + matched_file.suffix
        new_path = matched_file.parent / new_name
        rename_plan.append((matched_file, new_path))
    else:
        unmatched_files.append(file_a.name)

# Show scan summary
print(f"\n🔍 Scan Complete.")
print(f"✅ Matches found for {len(rename_plan)} file(s).")
print(f"❌ No matches for {len(unmatched_files)} file(s).")

# Show unmatched before rename prompt
if unmatched_files:
    print("\n📋 Files not renamed (no match or bad format):")
    for name in unmatched_files:
        print(" -", name)

    # Write unmatched to file
    with unmatched_file_path.open("w", encoding="utf-8") as f:
        f.write("Files not matched or skipped:\n")
        for name in unmatched_files:
            f.write(f"{name}\n")

    print(f"\n📝 List of unmatched files saved to: '{unmatched_file_path}'")

    # Copy-paste block
    print("\n📋 Copy-paste list:\n")
    print("\n".join(unmatched_files))

# Ask to proceed
confirm = input("\n👉 Proceed with renaming? [Y/N]: ").strip().lower()
if confirm == 'y':
    print("\n🔁 Renaming files...\n")
    for original, new_path in rename_plan:
        original.rename(new_path)
        print(f"✅ Renamed: {original.name} → {new_path.name}")
    input("\n✅ Renaming complete. Press Enter to exit.")
else:
    print("⏭️ Rename cancelled.")
    input("\n📌 Press Enter to exit.")
