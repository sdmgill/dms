import boto3
import time

client = boto3.client('dms', region_name='us-west-2')

glue = boto3.client(service_name='glue', region_name='us-west-2',
                    endpoint_url='https://glue.us-west-2.amazonaws.com')


def lambda_handler(event, context):
    # stop the DMS replication task
    client.stop_replication_task(
        ReplicationTaskArn='arn:aws:dms:us-west-2:062519970039:task:EKG4DKWY4RGPXI5DTYTMIFY6D4'
    )

    # wait 20 seconds for replication to drain
    time.sleep(20)

    # start Glue job
    glue.start_job_run(JobName='mistar-pnct-incremental-dbo-position')

    return 'mistar-pnct-position-table DMS Task stopped and mistar-pnct-incremental-dbo-position job started!!'
