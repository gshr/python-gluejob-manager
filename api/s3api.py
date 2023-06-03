from fastapi import APIRouter,Depends
from .deps import s3_client
from botocore.client import BaseClient
from .models import S3Model
from botocore.exceptions import ClientError
s3router = APIRouter(tags=['s3api'])

@s3router.post('/bucket',description='s3 Bucket to store glue script')
def create_s3_bucket(bucket:S3Model=Depends(),
                     s3:BaseClient=Depends(s3_client)):
    try:
        s3.create_bucket(Bucket= bucket.bucketname,
                         CreateBucketConfiguration={'LocationConstraint':f'{bucket.region}'})
    except ClientError as e:
        print(e)
        return False
    return {
        "message": "Bucket created successfully",
        "bucket": bucket.bucketname
    }
    
    
@s3router.get('/bucket',description='List all s3 Bucket in account')   
def get_bucket(s3:BaseClient=Depends(s3_client)):
    try:
        response = s3.list_buckets()
        
    except ClientError as e:
        print(e)
        return False
    return response['Buckets']
    