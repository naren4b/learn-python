# Lesson 25 — DIY

Use your local `lab/app.py` and the lesson's virtual environment.

## Your Exercise

1. Create a Boto3 `Session` using your existing AWS profile and preferred region.
2. Call `sts.get_caller_identity()`; print only the account ID, not credentials.
3. Using an EC2 paginator, list instance IDs and state names in that region.
4. Handle AWS service and missing-credentials errors without changing resources.

Do not create, delete or change AWS resources in this exercise.
