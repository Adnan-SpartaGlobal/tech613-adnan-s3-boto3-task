import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "tech613-adnan-test-boto3"
S3_KEY = "test.txt"

if input(f"Delete {S3_KEY} from {BUCKET_NAME}? Type the bucket name to confirm: ") != BUCKET_NAME:
    raise SystemExit("Cancelled.")

s3 = boto3.client("s3")

try:
    s3.delete_object(Bucket=BUCKET_NAME, Key=S3_KEY)
    print(f"Deleted s3://{BUCKET_NAME}/{S3_KEY}")
except ClientError as e:
    print(f"Error deleting object: {e}")
