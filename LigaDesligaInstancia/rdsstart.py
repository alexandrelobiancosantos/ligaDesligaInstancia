import boto3
region = 'us-east-1'
rds = boto3.client('rds', region_name=region)
my_instances = ['rdsclaudio']
def lambda_handler(event, context):
    for instance in my_instances:
	    rds.start_db_instance(DBInstanceIdentifier=instance)
	    print('starting your RDS: ' + str(instance))