import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "tech613-adnan-test-boto3"

s3 = boto3.client("s3")
# Get region from AWS config (we already did some aws configure stuff before)
region = s3.meta.region_name

try:
    # Will pass as we are in the eu-west-1
    if region == "us-east-1":
        s3.create_bucket(Bucket=BUCKET_NAME)
    else:
        # Creates a bucket with bucket name and with a specific region
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={"LocationConstraint": region},
        )
    print(f"Bucket '{BUCKET_NAME}' created in {region}.")
except ClientError as e:
    print(f"Error creating bucket: {e}")
