import boto3
import sys
from pprint import pprint

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

    if opt == 1:
        instance_id = input("Enter your instance id: ")
        response = ec2_con_re.Instance(instance_id)
        # i-0812426246f4aa70b
        pprint(dir(response))
        print("Start Ec2 instance")
        response.start()

    elif opt == 2:
        instance_id = input("Enter your instance id: ")
        response = ec2_con_re.Instance(instance_id)
        print("Stopping Ec2 instance")
        response.stop()

    elif opt == 3:
        instance_id = input("Enter your instance id: ")
        response = ec2_con_re.Instance(instance_id)
        print("Terminate the instance")
        response.terminate()

    elif opt == 4:
        print("Thank you for using script")
        sys.exit()

    else:
        print("your option is invalid")
