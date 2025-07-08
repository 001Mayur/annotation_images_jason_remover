import os

# Set your directory path
folder = r"D:\final_dataset_damage\Annotations"

# Get all filenames in the folder
all_files = os.listdir(folder)

# Separate image and json files
image_files = {os.path.splitext(f)[0] for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))}
json_files = [f for f in all_files if f.lower().endswith('.json')]

# Loop over jsons and delete if corresponding image doesn't exist
for json_file in json_files:
    base_name = os.path.splitext(json_file)[0]
    if base_name not in image_files:
        json_path = os.path.join(folder, json_file)
        os.remove(json_path)
        print(f"Deleted: {json_path}")

print("✅ Cleanup complete!")
