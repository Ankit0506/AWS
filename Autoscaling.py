import boto3
from pprint import pprint
import sys

#aws_mag_con_root=boto3.session.Session(profile_name="ankit")
# sts_con_cli=aws_mag_con_root.client(service_name="sts")
# response=sts_con_cli.get_caller_identity()
# print(response['Account'])

aws_mag_con_root=boto3.session.Session(profile_name="ankit")
ec2_con_cli=aws_mag_con_root.client(service_name="ec2",)
response=ec2_con_cli.describe_instances()['Reservations']
for each_item in response:
    for each in each_item['Instances']:
        print(each['ImageId'])

# aws_mag_con_root=boto3.session.Session(profile_name="ankit")
# ec2_con_cli=aws_mag_con_root.client(service_name="ec2")
# response=ec2_con_cli.describe_volumes()
# #pprint(response)
# for each_item in response:
#         print(response)

#
# aws_mag_con_root=boto3.session.Session(profile_name="ankit")
# ec2_con_re=aws_mag_con_root.resource(service_name="ec2",region_name="ap-south-1")
# ec2_con_cli=aws_mag_con_root.client(service_name="ec2")
# while True:
#     print("This script perform the following actions on ec2 instances")
#     print("""
#         1.start
#         2.stop
#         3.terminate
#         4.Exit
#         """)
#     opt=int(input("Enter your option: "))
#     if opt==1:
#         instance_id=input("Enter your instance id: ")
#         print("Start Ec2 instance")
#     elif opt==2:
#         instance_id = input("Enter your instance id: ")
#         print("Stopping Ec2 instance")
#     elif opt==3:
#         instance_id = input("Enter your instance id: ")
#         print("Terminate the instance")
#     elif opt==4:
#         print("Thank you for using script")
#         sys.exit()
#     else:
#         print("your option is invalid")


