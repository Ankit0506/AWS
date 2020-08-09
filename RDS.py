import boto3
import botocore
import sys
import os


def main():
    BUCKET_NAME = 'test-bucket'
    TEST_FILE = '/tmp/test-my-bucket.txt'
    TEST_FILE_KEY = 'test-my-bucket.txt'
    TEST_FILE_TARGET = '/tmp/test-my-bucket-target.txt'

client = boto3.client(service_name='s3')

#List Bucket
def my_list_bucket():
    bucket_list_response = client.list_buckets()

    if bucket_list_response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Bucket_list:" + ' '.join(p for p in [bucket['Name']
                                        for bucket in bucket_list_response['Buckets']]))
    else:
        print("List bucket failed")

my_list_bucket()
#Create Bucket
def create_bucket():
    BUCKET_NAME = 'test-bucket'
    create_bucket_response = client.create_bucket(Bucket=BUCKET_NAME,region_name="ap-south-1")

    if create_bucket_response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Successfully created bucket %s" % BUCKET_NAME)
    else:
        print("Create Bucket Failed")
create_bucket()
my_list_bucket()