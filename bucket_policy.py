import boto3
import json

s3 = boto3.client('s3')
bucket_name = 'ankit-123456764'

bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': "arn:aws:s3:::%s/*" % bucket_name
}]
}
bucket_policy = json.dumps(bucket_policy)
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)



# Call to S3 to retrieve the policy for the given bucket
result = s3.get_bucket_policy(Bucket='ankit-123456764')
print(result)