import boto3,pprint

session = boto3.session.Session(profile_name="ankit")
iam_res = session.resource("ec2")
iam_cli = session.client("ec2")

paginator= iam_cli.get_paginator("describe_instances")

for each in paginator.paginate():
        print(each)