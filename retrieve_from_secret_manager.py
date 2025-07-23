import boto3
import json

client = boto3.client('secretsmanager', region_name='us-east-1')

response = client.get_secret_value(SecretId='terraform_cred')
secrets = json.loads(response['SecretString'])

access_key = secrets['aws_access_key_id']
secret_key = secrets['aws_secret_access_key']

print("Access Key:", access_key)
print("Secret Key:", secret_key)
