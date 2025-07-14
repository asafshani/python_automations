import os
import datetime

# Function to bulk rename files in a directory
def rename_files(folder_path, prefix='', suffix='', use_timestamp=False, start_number=1):
    # Step 1: Check if folder is valid
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    # Step 2: Create a list to store file names (excluding folders)
    files = []  # Start with an empty list
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            files.append(item)

    # Optional: sort files alphabetically for consistent renaming order
    files.sort()

    # Step 3: Loop through each file and rename
    for idx, old_name in enumerate(files, start=start_number):
        name, ext = os.path.splitext(old_name)

        # Optional timestamp
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') if use_timestamp else ''

        # Build new file name
        new_name = f"{prefix}{idx}_{timestamp}{suffix}{ext}"

        # Construct full old and new paths
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} → {new_name}")

# === Program entry point ===
if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()
    prefix = input("Enter prefix (optional): ").strip()
    suffix = input("Enter suffix (optional): ").strip()
    use_ts = input("Add timestamp? (yes/no): ").strip().lower() == 'yes'
    start_num = input("Starting number (default 1): ").strip()
    start_num = int(start_num) if start_num.isdigit() else 1

    rename_files(folder, prefix=prefix, suffix=suffix, use_timestamp=use_ts, start_number=start_num)