import boto3

client = boto3.client('dms', region_name='us-west-2')

# grab arn from
client.stop_replication_task(
    ReplicationTaskArn='arn:aws:dms:us-west-2:062519970039:task:OTYMT6P7L4KQNOWV5Z7LBASSEQ'
)
