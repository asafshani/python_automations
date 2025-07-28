"""
Age-Based Backup Script:
Copies files from a source folder to a backup folder
if they're older than a user-defined number of days.
"""

import os
import shutil
import time

# Ask the user to enter the source directory
SOURCE_DIR = input("Enter the source folder path: ").strip()

# Ask the user to enter the backup directory
BACKUP_DIR = input("Enter the backup folder path: ").strip()

# Ask the user how many days old the files should be to qualify for backup
try:
    DAYS_OLD = int(input("Enter the number of days to consider a file old: "))
except ValueError:
    print("Invalid input. Using default of 30 days.")
    DAYS_OLD = 30

# Get the current time in seconds
current_time = time.time()

# Create the backup directory if it doesn't exist
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

# Loop through the files in the source directory
for filename in os.listdir(SOURCE_DIR):
    file_path = os.path.join(SOURCE_DIR, filename)

    # Make sure it's a file and not a folder
    if os.path.isfile(file_path):
        # Calculate file age in days
        file_age = (current_time - os.path.getmtime(file_path)) / 86400

        # If the file is old enough, copy it to the backup directory
        if file_age > DAYS_OLD:
            shutil.copy2(file_path, BACKUP_DIR)
            print(f"Backed up: {filename}")
