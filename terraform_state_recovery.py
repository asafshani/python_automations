# terraform_state_recover.py
# This script connects to an S3 backend storing a Terraform state file,
# lists previous versions (if versioning is enabled), and downloads a recovered
# version of the state file to help recover from corruption or misconfiguration.
# It now prompts the user to input the S3 bucket name and file path manually.

import boto3  # AWS SDK for Python
import sys    # For exiting the script if something goes wrong

def recover_state():
    # Ask the user for the bucket name
    BUCKET_NAME = input("Enter your S3 bucket name: ")

    # Ask the user for the state file path (key) in the bucket
    STATE_KEY = input("Enter the Terraform state file path in the bucket (e.g., env/dev/terraform.tfstate): ")

    # Set the name of the local file to save the recovered version
    DESTINATION_FILE = "terraform.tfstate.recovered"

    # Connect to AWS S3 using default credentials (from environment or IAM role)
    s3 = boto3.client('s3')

    # List all versions of the specified state file
    print(f"\nListing versions for: s3://{BUCKET_NAME}/{STATE_KEY}")
    versions = s3.list_object_versions(Bucket=BUCKET_NAME, Prefix=STATE_KEY)

    # Extract the 'Versions' list from the response
    version_items = versions.get('Versions', [])
    if not version_items:
        print("No previous versions found.")
        sys.exit(1)

    # Try to download older versions one by one, skipping the latest
    for version in version_items[1:]:  # Skip latest version (index 0)
        version_id = version['VersionId']
        print(f"Trying version ID: {version_id}")

        try:
            s3.download_file(
                Bucket=BUCKET_NAME,
                Key=STATE_KEY,
                Filename=DESTINATION_FILE,
                ExtraArgs={'VersionId': version_id}
            )
            print(f"\n✅ Recovered state file saved as: {DESTINATION_FILE}")
            return
        except Exception as e:
            print(f"⚠️ Error downloading version {version_id}: {e}")

    # If no version succeeded, notify the user
    print("No valid version could be recovered.")
    sys.exit(1)

# This makes sure the function runs only when you run the script directly
if __name__ == "__main__":
    recover_state()
