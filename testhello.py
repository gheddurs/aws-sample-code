import datetime
import os

import boto3

FILE_NAME = "hello.txt"
s3 = boto3.resource("s3")


def copy_file_to_destination():
    new_file_name = f"{FILE_NAME.split('.')[0]}_updated.txt"
    s3.Bucket(os.environ["DESTINATION_BUCKET"]).upload_file(
        f"/tmp/{FILE_NAME}", new_file_name
    )


def fetch_file_from_source():
    s3.Bucket(os.environ["SOURCE_BUCKET"]).download_file(FILE_NAME, f"/tmp/{FILE_NAME}")


def update_file():
    with open(f"/tmp/{FILE_NAME}", "a") as f:
        my_str = f"\nI read this file at {datetime.datetime.now()}!"
        f.write(my_str)


def handler(event, context):
    fetch_file_from_source()
    update_file()
    copy_file_to_destination()
