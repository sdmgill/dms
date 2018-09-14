import boto3

client = boto3.client('dms', region_name='us-west-2')

# grab arn from
client.start_replication_task(
    ReplicationTaskArn='arn:aws:dms:us-west-2:062519970039:task:3GR6RQOPPKT273VPKZ5H6C44HM',
    StartReplicationTaskType = 'reload-target'
)