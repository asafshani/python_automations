import boto3
import json

sqs = boto3.client('sqs') # creates an SQS client object using boto3 allowing your code to interact with SQS. 
QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/240617603981/image-processing-queue'

def lambda_handler(event, context):  #event contains the data passed to the function, in this case S3 event details.
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        message = json.dumps({'bucket': bucket, 'key': key}) #converts the pythogn dictionary into a JSON string
        sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=message)
    return {'status': 'Message sent to SQS'}
