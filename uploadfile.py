import boto3
import boto

# s3 = boto3.client('s3',region_name = 'ap-south-1')
# s3.create_bucket(Bucket='ankit-123456764',CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})


s3 = boto3.resource('s3')
BUCKET = "ankit-123456764"
s3.Bucket(BUCKET).upload_file("C:/Users/g703265/Desktop/13/Capture.JPG","ankit123")
print("Done " + BUCKET)

