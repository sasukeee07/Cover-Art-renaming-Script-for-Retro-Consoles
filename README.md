# Cover-Art-renaming-Script-for-Retro-Consoles
This script helps rename GBA cover images so they exactly match the ROM filenames — required for cover art to work correctly in Garlic OS (e.g., on Anbernic RG35XX). Just drop your files into folders, run the script, and you're done!
---

```markdown
# 🕹️ GBA Cover Image Renaming Script

This Python script automatically renames your GBA cover images to match your ROM filenames — perfect for organizing your game collection or frontend display!

---

## 📁 Folder Structure

Create a folder with this structure:

```

Main Folder/

├── Folder A → Your `.gba` ROM files

├── Folder B → Your cover images (`.jpg`, `.png`, etc.)

├── Folder C → Leave empty (used for unmatched logs)

└── gba\_renamer\_script.py → The Python script


````

---

## 🔧 Setup Steps

1. **Create a Main Folder** anywhere on your PC.
2. Inside it:
   - Place all your `.gba` ROMs in **Folder A**
   - Place all cover images in **Folder B**
   - Leave **Folder C** empty
   - Place the `Rename_ROM_files.py` file in the main folder

3. **Edit the Script**:
   - Open `Rename_ROM_files.py` in any text editor.
   - Find and update the folder paths:

     ```python
     folder_a = Path(r"D:\YourPath\Main Folder\Folder A")
     folder_b = Path(r"D:\YourPath\Main Folder\Folder B")
     unmatched_output_dir = Path(r"D:\YourPath\Main Folder\Folder C")
     ```

   - Save and close the script.

---

## ▶️ Running the Script

- **Option 1**: Double-click the Python script  
- **Option 2**: Run it via terminal or command line:

  ```bash
  python Rename_ROM_files.py
````

---

## ✅ What It Does

* Finds and renames cover images to match ROM filenames (ignoring file extensions and case)
* Keeps the original image format (e.g., `.jpg`, `.png`)
* Saves a list of unmatched image files in `Folder C/unmatched_files.txt`

---

## 💡 Example

**Before:**

* ROM: `0001 Pokemon Red.gba`
* Cover: `pokemon red.jpg`

**After:**

* Renamed cover: `0001 Pokemon Red.jpg`

---

## 🎉 You're Done!

Now your ROMs and covers are perfectly matched. Any unmatched files will be listed for review.

---


