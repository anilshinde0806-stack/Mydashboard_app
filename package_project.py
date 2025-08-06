import os
import zipfile

# Change this to your Django project folder name
project_name = "mydashboard"
zip_file_name = f"{project_name}.zip"

# Folders to exclude from the zip
exclude_dirs = ["__pycache__", ".venv", "env", ".git"]
exclude_files = [".DS_Store", "db.sqlite3"]

def zipdir(path, ziph):
    # Walk the directory tree
    for root, dirs, files in os.walk(path):
        # Exclude unwanted folders
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            if file in exclude_files:
                continue
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, os.path.dirname(path))
            ziph.write(full_path, relative_path)

# Create zip file
with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir(project_name, zipf)

print(f"✅ Zipped '{project_name}' into '{zip_file_name}' successfully!")
