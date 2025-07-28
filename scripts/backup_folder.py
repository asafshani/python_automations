import os
import zipfile
import datetime

# Function to create a timestamped zip backup of the target folder
def backup_folder(folder_path): 
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return  

    # Get folder name and current timestamp
    folder_name = os.path.basename(os.path.abspath(folder_path))
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_filename = f"{folder_name}_backup_{timestamp}.zip"

    # Create zip file
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Preserve folder structure inside zip
                arcname = os.path.relpath(file_path, folder_path)
                backup_zip.write(file_path, arcname)

    print(f"✅ Backup created: {zip_filename}")

# Ask the user for the folder path to back up
target_folder = input("Enter folder path to back up: ")
backup_folder(target_folder)
