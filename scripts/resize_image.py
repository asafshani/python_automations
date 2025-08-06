import boto3
import json
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        body = json.loads(record['body'])
        bucket = body['bucket']
        key = body['key']
        
        # Download image
        response = s3.get_object(Bucket=bucket, Key=key)
        image_data = response['Body'].read()
        
        # Resize image
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((200, 200))
        
        # Save to buffer
        buffer = io.BytesIO()
        image.save(buffer, format='JPEG')
        buffer.seek(0)
        
        # Upload to resized bucket
        s3.put_object(Bucket='photo-resized-bucket', Key=key, Body=buffer, ContentType='image/jpeg')
        
    return {'status': 'Image resized and uploaded'}

