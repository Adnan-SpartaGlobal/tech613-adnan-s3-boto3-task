import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "tech613-adnan-test-boto3"
S3_KEY = "test.txt"
DOWNLOAD_AS = "downloaded_test.txt"

s3 = boto3.client("s3")

try:
    # Calls S3_KEY and then saves the file associated with the key in DOWLOADED_AS
    s3.download_file(BUCKET_NAME, S3_KEY, DOWNLOAD_AS)
    print(f"Downloaded s3://{BUCKET_NAME}/{S3_KEY} to {DOWNLOAD_AS}")
except ClientError as e:
    print(f"Error downloading file: {e}")
