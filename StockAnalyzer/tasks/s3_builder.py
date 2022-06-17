import os
import logging
from datetime import datetime as dt
import boto3
from botocore.exceptions import ClientError

logging.basicConfig(filename='../logs/{}_log'.format(dt.strftime(dt.now(),'%Y%m%d')))

def aws_credentials():
    usr_path = os.path.expanduser('~')
    f = os.path.join(usr_path,'.aws')
    aws_files = os.listdir(f)
    if 'credentials' in aws_files:
        print('aws config all set!')
        with open(os.path.join(f,'config')) as f:
            region_ = f.read().split('\n')
        for r in region_:
            if 'region' in r :
                region = (r.split('='))[1]
                return region
            else:
                pass
    else:
        print('failure to configure AWS CLI. Please configure and then try running again.')
        return False

#from the boto3 docs
def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        logging.log(1, 'An error occurred on {}: {}'.format(dt.now(), e))
        return False
    return True

def s3_create(bucket_name):
    r = aws_credentials()
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')

    response = s3.list_buckets()
    print(response)
    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        if bucket['Name'] == bucket_name:
            print('bucket already created!')
            pass
        else:
            try:
                create_bucket(bucket_name, region='us-east-2')
                with open('s3_success.txt','w') as f:
                    f.write('1')
                f.close()
            except Exception as e:
                logging.error(e)
                logging.log(1, 'An error occurred on {}: {}'.format(dt.now(), e))

def check_success(file):
    try:
        with open(file,'r') as f:
            l = f.readline()
            print(l)
            return True
    except (FileNotFoundError, FileExistsError) as e:
        print(e)
        return False