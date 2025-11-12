import os, shutil, pathlib

downloads = pathlib.Path(r"C:\Users\Ediku\Downloads")

rules = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Videos": [".mp4", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Documents": [".pdf", ".docx", ".txt", ".csv", ".rtf"],
    "Software": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".tar"],
    "Web Files": [".html", ".mhtml"],
    "Calendar": [".ics"],
    "Code": [".cpp", ".json", ".sav", ".tns", ".py"],
    "Temp": [".crdownload", "Unconfirmed"]
}

def find_folder(file):
    ext = file.suffix.lower()
    for folder, exts in rules.items():
        if ext in exts:
            return folder
    return "Misc"

for item in downloads.iterdir():
    if item.is_file():  # leave folders alone
        folder = find_folder(item)
        dest = downloads / folder
        dest.mkdir(exist_ok=True)

        target = dest / item.name
        if target.exists():
            base, ext = os.path.splitext(item.name)
            i = 1
            while (dest / f"{base}_{i}{ext}").exists():
                i += 1
            target = dest / f"{base}_{i}{ext}"

        try:
            shutil.move(str(item), str(target))
            print(f"Moved {item.name} → {folder}")
        except Exception as e:
            print(f"⚠️ Could not move {item.name}: {e}")
