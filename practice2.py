import boto3

client = boto3.client('ec2')
# t1 = client.describe_addresses()
# print(t1)

t1 =client.describe_aggregate_id_format(
    DryRun=True|False
)
print(t1)