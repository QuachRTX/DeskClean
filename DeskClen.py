import os
from shutil import move

source_path = f"{os.environ['UserProfile']}\Desktop"
destination_path = f"{os.environ['UserProfile']}\Desktop\DeskClean"
extensions = {
    "Documents": [".pdf", ".docx", ".doc", ".ppt", ".pptx", ".csv", ".ofx"],
    "Pictures": [".jpg", ".png", ".gif", ".webp", ".ico", ".tga", ".dds", ".jpeg"],
    "Zip": [".zip", ".rar", ".7z"],
    "Videos": [".avi", ".mp4", ".mov", ".webm", ".mkv", ".wmv", ".flv", ".3gp", ".mpeg", ".mpg", ".m4v"],
}

def move_file(filename, dest_folder):
    src_path = os.path.join(source_path, filename)
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    dest_path = os.path.join(destination_path, dest_folder, filename)
    if not os.path.exists(dest_path):
        move(src_path, dest_path)
    else:
        print(f"File {filename} already exists")

for filename in os.listdir(source_path):
    for dest_folder, exts in extensions.items():
        for ext in exts:
            if filename.endswith(ext):
                move_file(filename, dest_folder)
                break
    if filename.endswith(".tmp"):
        break

for entry in os.scandir(source_path):
    if os.path.isdir(entry.path) and not os.listdir(entry.path):
        os.rmdir(entry.path)
