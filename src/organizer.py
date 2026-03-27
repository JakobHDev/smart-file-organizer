import os
import shutil
from datetime import datetime

PRESETS = {
    "GameDev": {
        "Textures": [".png", ".jpg", ".jpeg", ".tga", ".exr", ".gif"],
        "Audio": [".wav", ".mp3", ".ogg"],
        "Models": [".fbx", ".obj", ".blend"],
        "Scripts": [".py", ".cs", ".cpp", ".h"],
        "UI": [".svg", ".ttf", ".otf"],
        "Video": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
        "Misc": []
    },

    "GraphicDesign": {
        "Images": [".png", ".jpg", ".jpeg", ".tiff", ".tif", ".bmp", ".gif", ".webp"],
        "Vectors": [".svg", ".ai", ".eps"],
        "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
        "Projects": [".psd", ".xcf", ".afphoto", ".afdesign"],
        "Palettes": [".ase", ".aco", ".clr"],
        "Exports": [".pdf"],
        "Video": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
        "Misc": []
    },

    "Documents": {
        "Documents": [".doc", ".docx", ".pdf", ".rtf"],
        "Spreadsheets": [".xls", ".xlsx", ".csv"],
        "Text": [".txt", ".md", ".json", ".xml", ".yaml", ".ini"],
        "Presentations": [".ppt", ".pptx"],
        "Archives": [".zip", ".rar", ".7z"],
        "Video": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
        "Misc": []
    }
}

def sort_by_type(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            ext = filename.split(".")[-1].lower()

            # Create folder for this file type
            type_folder = os.path.join(folder, ext.upper())
            os.makedirs(type_folder, exist_ok=True)

            # Move file
            shutil.move(file_path, os.path.join(type_folder, filename))


def sort_by_date(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            timestamp = os.path.getmtime(file_path)
            date = datetime.fromtimestamp(timestamp)

            year_folder = os.path.join(folder, str(date.year))
            month_folder = os.path.join(year_folder, date.strftime("%B"))

            os.makedirs(month_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(month_folder, filename))


def organize_folders_alphabetically(folder):
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)

        # Only process folders
        if os.path.isdir(item_path):

            # Skip alphabetical group folders (A, B, C, 0, 1, etc.)
            if len(item) == 1 and item.isalnum():
                continue

            first_char = item[0].upper()

            # Create the alphabetical group folder
            group_folder = os.path.join(folder, first_char)
            os.makedirs(group_folder, exist_ok=True)

            # If the folder is already inside the correct group, skip it
            if os.path.dirname(item_path) == group_folder:
                continue

            # Move the folder into its alphabetical group
            shutil.move(item_path, os.path.join(group_folder, item))


def organize_by_preset(folder, preset_name):
    rules = PRESETS[preset_name]

    for root, dirs, files in os.walk(folder):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            file_path = os.path.join(root, file)

            category = "Misc"
            for cat, extensions in rules.items():
                if ext in extensions:
                    category = cat
                    break

            dest_folder = os.path.join(folder, category)
            os.makedirs(dest_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(dest_folder, file))