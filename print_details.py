import csv

import boto3

aws_mag_con = boto3.session.Session(profile_name="ankit")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name='ap-south-1')
ec2_con_cli = aws_mag_con.client(service_name="ec2", region_name='ap-south-1')
cnt = 1
csv_ob = open("inventry.csv", "w", newline='')
csv_w = csv.writer(csv_ob)
csv_w.writerow(['cnt', 'Instance_id', 'Instance_type', 'Architecture', 'Private_IP'])
for i in ec2_con_re.instances.all():
    print(cnt, i.instance_id, i.instance_type, i.architecture, i.private_ip_address)
    csv_w.writerow([cnt, i.instance_id, i.instance_type, i.architecture, i.private_ip_address])
    cnt += 1
csv_ob.close()
