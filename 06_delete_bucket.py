import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "tech613-adnan-test-boto3"

if input(f"Delete bucket {BUCKET_NAME}? Type the bucket name to confirm: ") != BUCKET_NAME:
    raise SystemExit("Cancelled.")

s3 = boto3.client("s3")

try:
    s3.delete_bucket(Bucket=BUCKET_NAME)
    print(f"Bucket '{BUCKET_NAME}' deleted.")
except ClientError as e:
    print(f"Error deleting bucket: {e}")
