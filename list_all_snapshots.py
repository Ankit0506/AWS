import boto3

aws_mag_con = boto3.session.Session(profile_name="ankit")

ec2_cli = aws_mag_con.client('ec2')
response = ec2_cli.get_caller_identity()
my_id = response.get('Account')
for each in ec2_cli.snapshots.filters(OwnerIds=[]):
    print(each)
