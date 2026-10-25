"""Lesson 25: read-only AWS identity and paginated EC2 inventory."""

import os

import boto3
from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError, ProfileNotFound


def main() -> None:
    profile = os.getenv("AWS_PROFILE", "personal")
    region = os.getenv("AWS_DEFAULT_REGION", "ap-south-1")
    try:
        session = boto3.Session(profile_name=profile, region_name=region)
        identity = session.client("sts").get_caller_identity()
        print("AWS Account:", identity["Account"], "Region:", region)

        ec2 = session.client("ec2")
        count = 0
        for page in ec2.get_paginator("describe_instances").paginate():
            for reservation in page["Reservations"]:
                for instance in reservation["Instances"]:
                    print(instance["InstanceId"], instance["State"]["Name"])
                    count += 1
        print("Instances found:", count)
    except (BotoCoreError, ClientError, NoCredentialsError, ProfileNotFound) as exc:
        print(f"AWS read failed: {exc}")


if __name__ == "__main__":
    main()
