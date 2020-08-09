import boto3
import botocore

session = boto3.session.Session(profile_name="ankit")
iam_con_re = session.resource(service_name="iam")

for user in iam_con_re.users.all():
    print(user)
    print(user.user_name)
