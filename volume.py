import boto3

aws_mag_con = boto3.session.Session(profile_name="ankit")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name='ap-south-1')
ec2_con_cli = aws_mag_con.client(service_name="ec2", region_name='ap-south-1')
# f1_used={"Name": "Volume", "status": ["available"]}
#
# for each_volume in ec2_con_re.volumes.filter(Filters=[f1_used]):
#     if not each_volume.tags:
#         print(each_volume.id, each_volume.state)


for each_item in ec2_con_cli.describe_volumes()['Volumes']:
    if not "Tags" in each_item and each_item['State'] == 'in-use':
        print(each_item['VolumeId'])
        ec2_con_cli.delete_volume(each_item['VolumeId'])