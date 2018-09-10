import boto3

client = boto3.client('dms', region_name='us-west-2')


def lambda_handler(event, context):
    # resume DMS replication task. Important to Resume and not Start. Resume
    # will pick up where it left off. Start will re-initialize replication,
    # meaning it will generate another initial load, re-seed CDC and then begin
    # transfering the deltas

    client.start_replication_task(
        ReplicationTaskArn='arn:aws:dms:us-west-2:062519970039:task:EKG4DKWY4RGPXI5DTYTMIFY6D4',
        StartReplicationTaskType='resume-processing'
    )
    return 'mistar-pnct-position-table DMS task successfully resumed.'
