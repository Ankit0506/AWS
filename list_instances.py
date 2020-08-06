import boto3

ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print(instance.id, instance.state)

#i-0eb753bbaecb364e0