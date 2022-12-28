import boto3
region = 'us-east-1'
instances = ['i-0d50787ad72398073']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('starting your instances: ' + str(instances))