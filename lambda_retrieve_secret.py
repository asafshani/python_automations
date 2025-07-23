import boto3
import json

def lambda_handler(event, context):
    secret_name = "terraform_cred"
    region_name = "us-east-1"  # change to your region

    # Create Secrets Manager client
    client = boto3.client('secretsmanager', region_name=region_name)

    # Fetch the secret
    response = client.get_secret_value(SecretId=secret_name)
    secrets = json.loads(response['SecretString'])

    access_key = secrets['aws_access_key_id']
    secret_key = secrets['aws_secret_access_key']

    return {
        'AccessKeyId': access_key,
        'SecretAccessKey': secret_key
    }
