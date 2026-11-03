# tech613-adnan-s3-boto3-task

Managing AWS S3 from Python using **boto3**. Each script reproduces an AWS CLI command as a small Python script.

## What this project does

| Script | What it does | AWS CLI equivalent | boto3 method |
|---|---|---|---|
| `01_list_buckets.py` | Lists all buckets in the account | `aws s3 ls` | `list_buckets()` |
| `02_create_bucket.py` | Creates a bucket | `aws s3 mb` | `create_bucket()` |
| `03_upload_file.py` | Uploads `test.txt` to the bucket | `aws s3 cp test.txt s3://bucket` | `upload_file()` |
| `04_download_file.py` | Downloads the file as `downloaded_test.txt` | `aws s3 cp s3://bucket/test.txt .` | `download_file()` |
| `05_delete_file.py` | Deletes the file from the bucket | `aws s3 rm` | `delete_object()` |
| `06_delete_bucket.py` | Deletes the (empty) bucket | `aws s3 rb` | `delete_bucket()` |

## Prerequisites

- An Ubuntu VM (AWS EC2) with SSH access
- Python 3 and `python3-venv`
- AWS CLI installed and configured with `aws configure` (region `eu-west-1`)
- An IAM user with S3 permissions

## Setup

```bash
# Create and activate a virtual environment
sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate

# Install boto3
pip install boto3

# Check it installed
python -c "import boto3; print(boto3.__version__)"

# Check authentication works
aws sts get-caller-identity
```

boto3 reads credentials and the region automatically from `~/.aws/credentials` and `~/.aws/config`, so **no keys are stored in the code**.

Create a test file to upload:

```bash
echo This is the first line in a boto3 test file > test.txt
```

## Usage

Run the scripts in order:

```bash
python 01_list_buckets.py
python 02_create_bucket.py
python 03_upload_file.py
python 04_download_file.py
cat downloaded_test.txt
python 05_delete_file.py
python 06_delete_bucket.py
```

Scripts 5 and 6 ask you to type the bucket name before deleting anything.

### Expected output

```
$ python 02_create_bucket.py
Bucket 'tech613-adnan-test-boto3' created in eu-west-1.

$ python 03_upload_file.py
Uploaded test.txt to s3://tech613-adnan-test-boto3/test.txt

$ python 04_download_file.py
Downloaded s3://tech613-adnan-test-boto3/test.txt to downloaded_test.txt

$ python 05_delete_file.py
Deleted s3://tech613-adnan-test-boto3/test.txt

$ python 06_delete_bucket.py
Bucket 'tech613-adnan-test-boto3' deleted.
```

## How it works

- **Client:** `s3 = boto3.client("s3")` creates the S3 connection.
- **Region:** `s3.meta.region_name` returns the region saved by `aws configure`. It is not based on your IP or location.
- **Bucket names** are globally unique across all of AWS, lowercase, with no underscores.
- **LocationConstraint:** outside `us-east-1`, `create_bucket()` must be given `CreateBucketConfiguration={"LocationConstraint": region}`.
- **Object key:** the name of the object inside the bucket. Bucket + key together identify one object (`s3://bucket/key`).
- **Error handling:** each call is wrapped in `try / except ClientError` so AWS errors print a readable message.
- **Deleting:** a bucket must be empty before it can be deleted, and boto3 has no equivalent of `--force`, so the objects are deleted first (Script 5, then Script 6).

## Safety notes

- Bucket names are global and the AWS account is shared. Check `BUCKET_NAME` before running the delete scripts so you don't delete someone else's bucket.
- `delete_object` does not raise an error if the key doesn't exist. Verify with `aws s3 ls s3://tech613-adnan-test-boto3`.
- Never put access keys in a script or push `~/.aws/` to GitHub. Check with:

  ```bash
  grep -r "AKIA" . --exclude-dir=venv
  ```

  This should print nothing.
- `.gitignore` excludes `venv/`, `__pycache__/`, `*.pyc`, `downloaded_test.txt` and `.env`.

## Common errors

| Error | Cause / fix |
|---|---|
| `externally-managed-environment` | Using `pip` outside a venv. Activate the venv |
| `ModuleNotFoundError: No module named 'boto3'` | venv not activated (`source venv/bin/activate`) |
| `NoCredentialsError` | `aws configure` not done, or run as a different user |
| `AccessDenied` | IAM user lacks S3 permissions |
| `BucketAlreadyExists` | Name taken by someone else. Pick a more unique one |
| `IllegalLocationConstraintException` | Missing `LocationConstraint` outside `us-east-1` |
| `BucketNotEmpty` | Delete the objects first (Script 5) |

## Project structure

```
tech613-adnan-s3-boto3-task/
├── 01_list_buckets.py
├── 02_create_bucket.py
├── 03_upload_file.py
├── 04_download_file.py
├── 05_delete_file.py
├── 06_delete_bucket.py
├── test.txt
├── .gitignore
└── README.md
```
