import boto3, time

aws_con = boto3.session.Session(profile_name="ankit")
ec2_con_re = aws_con.resource(service_name="ec2", region_name='ap-south-1')
ec2_con_cli = aws_con.client(service_name="ec2", region_name='ap-south-1')

my_inst_obg = ec2_con_re.Instance("i-0812426246f4aa70b")

print("Starting the instance")
my_inst_obg.start()
my_inst_obg.describe_instances()
print("Now your instance is running")

# while True:
#     my_inst_obg=ec2_con_re.Instance("i-0812426246f4aa70b")
#     if my_inst_obg.state['Name'] =='running':
#         break
#     print("Waiting for running status")
#     time.sleep(5)
# print(my_inst_obg.state)

print("Instance is running")
