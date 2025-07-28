# This script assumes an IAM role in a separate AWS account and uses temporary credentials
# to access an Amazon S3 bucket. It lists all objects in the specified bucket using boto3.


import boto3

# Step 1: Assume the role in Account B
sts_client = boto3.client('sts')

response = sts_client.assume_role(
    RoleArn='arn:aws:iam::<ACCOUNT_B_ID>:role/CrossAccountS3Access',
    RoleSessionName='CrossAccountSession'
)

# Step 2: Extract temporary credentials
credentials = response['Credentials']

# Step 3: Use credentials to access the S3 bucket
s3_client = boto3.client(
    's3',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken']
)

# Step 4: Example — list objects in the target bucket
bucket_name = 'your-bucket-name'
response = s3_client.list_objects_v2(Bucket=bucket_name)

if 'Contents' in response:
    print(f"Objects in bucket '{bucket_name}':")
    for obj in response['Contents']:
        print(f"- {obj['Key']}")
else:
    print(f"No objects found in bucket '{bucket_name}'.")
