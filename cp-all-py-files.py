from secrets import access_key, secret_access_key
from datetime import date, datetime
import boto3
import os


from botocore.utils import datetime2timestamp

client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)

for file in os.listdir():
    if '.py' in file:
        upload_file_bucket = 'cp-files-10022021'
        upload_file_key = 'python/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
        print(file + ' <- files has been uploaded to s3 bucket. ' + upload_file_bucket + "  :" + str(datetime.now()))


