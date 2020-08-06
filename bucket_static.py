import boto3

s3 = boto3.client('s3')
# result = s3.get_bucket_website(Bucket='ankit-123456764')

website_configuration = {
    'ErrorDocument': {'Key':'error.html'},
    'IndexDocument': {'Suffix':'index.html'}
}

s3.put_bucket_website(
    Bucket='ankit-123456764',
    WebsiteConfiguration=website_configuration
)

