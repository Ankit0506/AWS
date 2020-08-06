import boto3

s3 = boto3.client('s3')
s3.delete_bucket_policy(Bucket='ankit-123456764')