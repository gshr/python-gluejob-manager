from botocore.client import BaseClient
from fastapi import APIRouter, HTTPException, File, UploadFile, Depends
from .deps import s3_client, glue_client
from .models import GlueModel
from .helper import create_glue_job

router = APIRouter(tags=['glueapi'])


@router.get('/jobs')
def get_jobs(glue: BaseClient = Depends(glue_client)):
    response = glue.get_jobs()
    print(response)
    if len(response['Jobs']) == 0:
        raise HTTPException(status_code=404, detail="No Glue Jobs Available")
    return response


@router.post('/job', status_code=201)
def create_job(job: GlueModel = Depends(),
               file: UploadFile = File(...),
               s3: BaseClient = Depends(s3_client),
               glue: BaseClient = Depends(glue_client)):
    file_name = file.filename
    res = s3.upload_fileobj(file.file,job.bucketname, file_name)
    scriptlocation = f"s3://{job.bucketname}/{file.filename}"
    
    try:

        response = create_glue_job(glue=glue,
                                jobname=job.jobname,
                                scriptlocation=scriptlocation,
                                glueversion=job.glueversion,
                                numberofworkers=job.numberofworkers,
                                workertype=job.workertype,
                                role=job.role)
        return response
    except Exception as e:
        return e


@router.post('/startjob/{jobname}')
def start_job(jobname: str):
    return f'Job Started {jobname}'
