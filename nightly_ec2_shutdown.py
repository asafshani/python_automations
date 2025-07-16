import boto3
from datetime import datetime

# Initialize EC2 resource using default region from Lambda's execution environment
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # Log timestamp each time the function is triggered (useful for CloudWatch visibility)
    print("Lambda triggered at:", datetime.utcnow().isoformat())

    # Define filters to find EC2 instances:
    # - Tagged with Shutdown=true
    # - Currently in 'running' state
    filters = [
        {'Name': 'tag:Shutdown', 'Values': ['true']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]
    print("Using filters:", filters)

    # Query EC2 instances that match the filters
    instances = ec2.instances.filter(Filters=filters)

    # Extract instance IDs from the filtered results
    instance_ids = [i.id for i in instances] # list comprehension:
    #for every ec2 instance in the object i in the filtered results called instances,extarct its id and collect thos into a list

    # If matching instances are found, stop them
    if instance_ids:
        print(f"Found {len(instance_ids)} instance(s) to stop: {instance_ids}")
        ec2.instances.filter(InstanceIds=instance_ids).stop()
    else:
        # Log when no instances match criteria
        print("No instances to stop.")
