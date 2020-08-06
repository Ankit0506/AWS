import boto3

s3 = boto3.client('s3')
bucket_lifecycle = s3.BucketLifeCycle('ankit-123456764')
print(bucket_lifecycle)