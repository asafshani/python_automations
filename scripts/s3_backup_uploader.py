import boto3
import os
from botocore.exceptions import NoCredentialsError

# Configuration
BUCKET_NAME = 'asaftestingboto3'
FOLDER_PATH = '/home/asaf/course/python_automations/backup'
TAG_KEY = 'Project'
TAG_VALUE = 'BackupAutomation'

def upload_to_s3(file_path, bucket, key):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket, key)
        s3.put_object_tagging(
            Bucket=bucket,
            Key=key,
            Tagging={'TagSet': [{'Key': TAG_KEY, 'Value': TAG_VALUE}]}
        )
        print(f"Uploaded: {file_path} → s3://{bucket}/{key}")
    except NoCredentialsError:
        print("AWS credentials not found.")
    except Exception as e:
        print(f"Failed to upload {file_path}: {e}")

def run():
    if not os.path.isdir(FOLDER_PATH):
        print(f"Backup folder not found: {FOLDER_PATH}")
        return

    files = [f for f in os.listdir(FOLDER_PATH) if f.endswith('.zip')]
    # #alternative:
    # files = []  # start with an empty list

    # for f in os.listdir(FOLDER_PATH):
    #     if f.endswith('.zip'):
    #        files.append(f)  # add it to the list if it ends with .zip


    if not files: #if the list is empty its considered to be false in a condition
        print("No backup files found.")
        return

    for filename in files:
        full_path = os.path.join(FOLDER_PATH, filename)
        upload_to_s3(full_path, BUCKET_NAME, filename)

if __name__ == '__main__':   #If this script is being run directly by the user (not imported by another script), then do the stuff below.”
    run()
