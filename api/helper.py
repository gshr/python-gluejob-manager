import json


def create_glue_job(glue,
                    jobname,
                    scriptlocation,
                    glueversion,
                    numberofworkers,
                    workertype,
                    role):
    response = glue.create_job(
        Name=jobname,
        Role=role,
        Command={
            'Name': 'glueetl',
            'ScriptLocation': scriptlocation,
            'PythonVersion': '3'
        },
        DefaultArguments={
            '--job-bookmark-option': 'job-bookmark-enable'
        },
        MaxRetries=0,
        GlueVersion=glueversion,
        NumberOfWorkers=numberofworkers,
        WorkerType=workertype
    )
    return json.dumps(response, indent=4, sort_keys=True, default=str)
