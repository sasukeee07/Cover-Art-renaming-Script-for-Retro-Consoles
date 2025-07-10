# Cover-Art-renaming-Script-for-Retro-Consoles
A simple Python script that renames  cover images to match ROM filenames using fuzzy matching. Perfect for organizing game libraries and frontends.
Here's a ready-to-use **`README.md`** file for your GitHub repository, based on the contents of your `Gameboy_github.docx`:

---

```markdown
# 🕹️ GBA Cover Image Renaming Script

This Python script helps automatically rename Game Boy Advance (GBA) cover image files to match the filenames of your ROMs — ideal for ROM managers and frontends like EmulationStation, LaunchBox, or Skraper.

---

## 📁 Folder Structure & Setup

### 🔧 Step-by-Step Instructions

1. **Create a Main Folder** — This will contain all your files.
2. Inside it, create the following:

```

Main Folder/
├── Folder A (ROMs)           → Paste your .gba files here
│   └── Example: `0001 Pokemon Red.gba`
├── Folder B (Cover Images)   → Paste your cover images here
│   └── Example: `pokemon red.jpg`
├── Folder C (Output)         → Leave this empty
│   → This will store `unmatched_files.txt`
└── gba\_renamer\_script.py     → Paste the script here

````

---

## 🔁 What the Script Does

- Compares image names in Folder B with ROM filenames in Folder A.
- Ignores case and file extensions.
- If a close match is found, the image is renamed to match the ROM filename (keeping the image's extension).
- Unmatched images are logged in `unmatched_files.txt` inside Folder C.

---

## ✅ Example

### Input:

- `Folder A:` `0001 Pokemon Red.gba`
- `Folder B:` `pokemon red.jpg`

### Output:

- Renamed: `0001 Pokemon Red.jpg` (moved/updated in Folder B)
- Unmatched (if any): logged in `Folder C/unmatched_files.txt`

---

## 🛠️ How to Use

1. Open `gba_renamer_script.py` in a text editor.
2. Find the section:
   ```python
   # Set your folder paths
   folder_a = Path(r"...")
   folder_b = Path(r"...")
   unmatched_output_dir = Path(r"...")
````

3. Replace the paths with your local directories (e.g., `D:\MyGBA\Folder A`)
4. Save the file.

---

## ▶️ Run the Script

Run the script using one of these methods:

* **Double-click** the `.py` file (if Python is associated)
* **Or** use terminal/command prompt:

  ```bash
  python gba_renamer_script.py
  ```

---

## 🎉 Done!

* All matching cover images will be renamed to match ROM files.
* All unmatched images will be listed in `Folder C/unmatched_files.txt`.

---

## 📜 License

MIT License. Free to use and modify.

---

## 🙌 Contributions Welcome!

Feel free to fork, improve, and submit pull requests. If you find bugs or want extra features (e.g., support for other platforms), open an issue!

```

---

Let me know if you want to include badges (Python version, License, etc.), screenshots, or a demo GIF!
```
