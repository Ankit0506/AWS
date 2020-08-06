import boto3
import sys

aws_mag_con_root = boto3.session.Session(profile_name="ankit")
ec2_con_re = aws_mag_con_root.resource(service_name="ec2", region_name="ap-south-1")
ec2_con_cli = aws_mag_con_root.client(service_name="ec2", region_name="ap-south-1")
while True:
    print("This script perform the following actions on ec2 instances")
    print("""
        1.start
        2.stop
        3.terminate
        4.Exit
        """)

    opt = int(input("Enter your option: "))

    if opt==1:
        instance_id=input("Enter you Ec2 instanceid:" )
        response=ec2_con_re.In