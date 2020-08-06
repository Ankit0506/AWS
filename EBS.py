import boto3

ids = ['i-0344ec55ccd320c8b','i-0e37faba63dd7e239']
ec2 = boto3.resource('ec2')

ec2.instances.filter(InstanceIds = ids).terminate()
