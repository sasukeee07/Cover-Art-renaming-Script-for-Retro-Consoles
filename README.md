# Cover-Art-renaming-Script-for-Retro-Consoles
A simple Python script that renames  cover images to match ROM filenames using fuzzy matching. Perfect for organizing game libraries and frontends.
Here's a ready-to-use **`README.md`** file for your GitHub repository, based on the contents of your `Gameboy_github.docx`:

---

🕹️ GBA Cover Image Renaming Script
This Python script helps automatically rename GBA cover image files to match the filenames of your ROMs.
📁 How It Works
You need 3 folders:
1.	Folder A (ROMs) – Contains your .gba game ROMs (e.g., 0001 Pokemon Red.gba)
2.	Folder B (Covers) – Contains the matching cover images (e.g., pokemon red.jpg)
3.	Folder C  (Output) – This will store a text file listing any unmatched cover images that couldn’t be renamed.
🔁 What the Script Does
•	It compares each image name in Folder B with ROM names in Folder A(ignoring case and file extensions).
•	If a close match is found, the image is renamed to match the ROM filename, but with the image file extension.
•	Images that don’t match any ROM are logged in a .txt file inside Folder C.
✅ Example
Input:
•	Folder A: 0001 Pokemon Red.gba
•	Folder B: pokemon red.jpg
Output:
•	Renamed image: 0001 Pokemon Red.jpg

Of course! Here’s the full description with clear steps for setup and usage, perfect for sharing on a forum or with others:
________________________________________
🕹️ GBA Cover Image Renaming Script
This Python script automatically renames your GBA cover images to match the corresponding ROM filenames — making it perfect for organizing game libraries or frontends.
________________________________________
📁 Folder Structure & Setup
🔧 Step-by-Step Instructions:
1.	Create a main folder — This will contain everything.
2.	Inside the main folder, create the following:
o	Folder A → Paste your .gba ROM files here
Example: 0001 Pokemon Red.gba
o	Folder B → Paste your cover images here
Example: pokemon red.jpg
o	Folder C → Leave this empty; this is where unmatched image names will be saved in a .txt file
o	Python Script → Paste the script file here
Your folder should now look like this:
Main Folder/
├── Folder A (ROMs)
├── Folder B (Cover Images)
├── Folder C (Unmatched Output)
└── gba_renamer_script.py
________________________________________
🛠️ How to Use
1.	Right-click on the Python script (.py file) and choose Edit with Notepad (or any text editor).
2.	Scroll down to where it says:
3.	# Set your folder paths
4.	Replace the folder paths with the full path of your Folder A, B, and C. Example:
5.	folder_a = Path(r"D:\YourPath\Main Folder\Folder A")
6.	folder_b = Path(r"D:\YourPath\Main Folder\Folder B")
7.	unmatched_output_dir = Path(r"D:\YourPath\Main Folder\Folder C")
8.	Save the file.
________________________________________
▶️ Run the Script
•	Double-click the .py file or run it using Python (python gba_renamer_script.py).
•	The script will:
o	Compare image names in Folder B with ROM names in Folder A
o	Rename matched images in Folder B to match ROMs (keeping image extensions like .jpg)
o	Log unmatched image files into a unmatched_files.txt file inside Folder C
________________________________________
🎉 Done!
Once the script finishes running:
•	All matching cover images will be renamed properly.
•	Any covers that didn't match a ROM will be listed in unmatched_files.txt.
Enjoy your neatly organized ROM and cover collection!
________________________________________



