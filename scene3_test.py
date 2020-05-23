import boto3
from pprint import pprint


session = boto3.session.Session(profile_name='kerrigan')
ec2_cli = session.client(region_name='us-east-1', service_name='ec2')
iam_cli = session.client(region_name='us-east-1', service_name='iam')

pprint(iam_cli.list_role_policies(RoleName='cg-ec2-mighty-role-cgid82ug7z7vkg')
