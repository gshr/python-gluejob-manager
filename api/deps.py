import boto3
from botocore.client import BaseClient


def s3_client() -> BaseClient:
    s3 = boto3.client('s3')
    return s3



def glue_client() -> BaseClient:
    glue = boto3.client('glue')
    return glue