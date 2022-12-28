import boto3
region = 'us-east-1'
instances = ['i-0b98a71157caba8f8']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('starting your instances: ' + str(instances))