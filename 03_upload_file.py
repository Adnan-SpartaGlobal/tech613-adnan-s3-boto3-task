import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "tech613-adnan-test-boto3"
LOCAL_FILE = "test.txt"
S3_KEY = "test.txt"

s3 = boto3.client("s3")

try:
    # Upload file to the bucket and give it a key called S3_KEY so you can access it later
    s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_KEY)
    print(f"Uploaded {LOCAL_FILE} to s3://{BUCKET_NAME}/{S3_KEY}")
except (ClientError, FileNotFoundError) as e:
    print(f"Error uploading file: {e}")
