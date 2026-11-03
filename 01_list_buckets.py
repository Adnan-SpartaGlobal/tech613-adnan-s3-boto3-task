# Install dependencies
import boto3
from botocore.exceptions import ClientError

# Connect to S3 service
s3 = boto3.client("s3")

try:
    # Get a list of all buckets
    response = s3.list_buckets()
    buckets = response["Buckets"]

    # If there are no buckets
    if not buckets:
        print("No buckets found.")
    
    # Show bucket names
    for bucket in buckets:
        print(bucket["Name"])
except ClientError as e:
    # Catch all errors
    print(f"Error listing buckets: {e}")
