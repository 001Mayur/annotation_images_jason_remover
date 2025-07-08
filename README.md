
# 🧹 Dataset Cleanup Script — Remove Orphaned Images and JSON Files

This Python script automatically **cleans your annotation dataset folder** by deleting:

- 🖼️ **Image files** (`.jpg`, `.jpeg`, `.png`) that **don’t have a corresponding `.json` file**
- 📄 **JSON annotation files** that **don’t have a corresponding image file**

It’s especially helpful when using annotation tools like **LabelMe**, where each image must have a `.json` pair and vice versa.

---

## 📁 Folder Example Before Cleanup

```
dataset/
├── frame_0040413(48).json  ✅
├── frame_0040413(48).jpg   ✅
├── frame_0040413(49).json  ✅
├── frame_0040413(50).jpg   ❌ No JSON
├── frame_0040413(51).json  ❌ No Image
```

After cleanup, only correctly paired image+JSON files will remain.

---

## ✅ What This Script Does

- ✔️ Removes all `.json` files that **don't have a matching image**
- ✔️ Removes all image files that **don't have a matching `.json`**

> Ensures your dataset folder is **clean, consistent, and ready** for training or annotation tools.

---

## 🧠 How It Works

1. Extract the **base filenames** (e.g., `frame_0040413(48)`) from both image and JSON files.
2. Compare both lists.
3. Delete any file (image or JSON) that doesn’t have a matching pair.

---

## 🚀 How to Use

1. 🔁 **Update the folder path** in the script:
   ```python
   folder = r"C:\path\to\your\dataset"
   ```

2. ▶️ **Run the script**:
   ```bash
   python dataset_cleaner.py
   ```

3. 🧹 Output:
   ```
   Deleted orphaned image: frame_0040413(50).jpg
   Deleted orphaned JSON : frame_0040413(51).json
   ✅ Cleanup complete!
   ```

---

## 💻 Full Python Script

```python
import os

# Path to your dataset folder
folder = r"C:\path\to\your\dataset"

# List all files
all_files = os.listdir(folder)

# Get base names
json_bases = {os.path.splitext(f)[0] for f in all_files if f.lower().endswith('.json')}
image_exts = ('.jpg', '.jpeg', '.png')
image_bases = {os.path.splitext(f)[0] for f in all_files if f.lower().endswith(image_exts)}

# Delete orphaned JSON files
for f in all_files:
    if f.lower().endswith('.json'):
        base = os.path.splitext(f)[0]
        if base not in image_bases:
            os.remove(os.path.join(folder, f))
            print(f"Deleted orphaned JSON : {f}")

# Delete orphaned image files
for f in all_files:
    if f.lower().endswith(image_exts):
        base = os.path.splitext(f)[0]
        if base not in json_bases:
            os.remove(os.path.join(folder, f))
            print(f"Deleted orphaned image: {f}")

print("✅ Cleanup complete!")
```

---

## 🛡️ Safety Options

Want to **move files to backup** instead of deleting?
Replace this line:
```python
os.remove(os.path.join(folder, f))
```
with:
```python
import shutil
shutil.move(os.path.join(folder, f), r"C:\path\to\backup_folder")
```

---

## 📌 Requirements

- Python 3.6 or above
- No external libraries needed (only `os` module)

---

## 📄 License

This script is open-sourced under the [MIT License](https://opensource.org/licenses/MIT).  
Use it freely in personal or commercial projects.
