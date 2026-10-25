# Lesson 25 — AWS automation with Boto3

## Goal
Use the official AWS SDK for Python to inspect AWS resources without modifying them.

## Setup (WSL with uv)
From the repository root:

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r lesson-25-boto3/requirements.txt
AWS_PROFILE=personal AWS_DEFAULT_REGION=ap-south-1 .venv/bin/python lesson-25-boto3/25_boto3.py
```

Use an existing AWS profile with least-privilege permissions. Confirm the selected account before operating on resources. No access keys belong in this repository.

## Core API

| Boto3 operation | Purpose |
| --- | --- |
| `boto3.Session(profile_name=..., region_name=...)` | Explicit credential/profile and region context |
| `session.client("sts")` | AWS Security Token Service client |
| `sts.get_caller_identity()` | Identify the account and caller (read-only) |
| `session.client("ec2")` | EC2 service client |
| `ec2.get_paginator("describe_instances")` | Read all result pages |
| `botocore.exceptions.ClientError` | Service/API failures |

## Safe first example

```python
import boto3

session = boto3.Session(profile_name="personal", region_name="ap-south-1")
identity = session.client("sts").get_caller_identity()
print("Account:", identity["Account"])
```

## Pagination: EC2 instance inventory

`describe_instances` may return multiple pages. Use the SDK paginator, then traverse the nested `Reservations` and `Instances` collections:

```python
ec2 = session.client("ec2")
for page in ec2.get_paginator("describe_instances").paginate():
    for reservation in page["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance["InstanceId"], instance["State"]["Name"])
```

**Notes:** Boto3 returns ordinary Python dictionaries and lists. Credentials follow the AWS credential-provider chain; do not hardcode secrets. Account/region are controlled through your profile or environment. `ClientError` covers authorization and service errors; connection and credential errors need separate handling.

[DIY](diy.md) · [Reference](25_boto3.py) · [Official Boto3 sessions](https://docs.aws.amazon.com/boto3/latest/guide/session.html) · [Credentials](https://docs.aws.amazon.com/boto3/latest/guide/credentials.html) · [Paginators](https://docs.aws.amazon.com/boto3/latest/guide/paginators.html)
