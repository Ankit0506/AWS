import boto3

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(ImageId='ami-0ebc1ac48dfd14136',MinCount=1,MaxCount=1,
                                InstanceType='t2.micro')

print(instance[0].id)

