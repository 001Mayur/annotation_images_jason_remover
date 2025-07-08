import os

# Set your folder pathD
folder = r"D:\final_dataset_damage\pranjaliG"

# Get all files
all_files = os.listdir(folder)

# Get base names of JSON files
json_files = {os.path.splitext(f)[0] for f in all_files if f.lower().endswith('.json')}

# Target image extensions
image_exts = ('.jpg', '.jpeg', '.png')

# Loop through image files and delete if no matching JSON exists
for f in all_files:
    if f.lower().endswith(image_exts):
        base_name = os.path.splitext(f)[0]
        if base_name not in json_files:
            file_path = os.path.join(folder, f)
            os.remove(file_path)
            print(f"Deleted: {file_path}")

print("✅ Image cleanup complete!")
