import boto3,botocore

client = boto3.resource('s3')

try:
    client.create_bucket(Bucket='ankit-050619901',CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
except client.meta.client.exceptions.BucketAlreadyExists as err:
    print("Bucket {} already exists!".format(err.response['Error']['BucketName']))
    raise err