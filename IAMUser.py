import boto3,sys

def get_iam_client_obj():
    session=boto3.session.Session(profile_name="test")
    iam_client=session.client(service_name="iam",region_name="ap-south-1")
    return iam_client

def main():
    iam_client=get_iam_client_obj()
    iam_user_name="ankit.rai.0506@gmail.com"

    PolicyArn = "arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_client.create_user(Username=iam_user_name)
    except Exception as e:
        if e.response['Error']['Code'] =="EntityAlreadyExists":
            print("Already Iam User with {} is exist".format(iam_user_name))
            sys.exit(0)
        else:
            print("Please verify the following error and retry")
            print(e)
            sys.exit(0)
    response = iam_client.create_access_key(UserName=iam_user_name)



if __name__ == '__main__':
    main()
