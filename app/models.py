from pydantic import BaseModel
from enum import Enum
from typing import Optional


class GlueModel(BaseModel):
    jobname : str
    role : str 
    pythonversion : str = '3'
    description : Optional[str] 
    workertype : str = 'Standard'
    glueversion : str = '3.0'
    numberofworkers : int = 1
    role : str = 'admin-glue-role-admin'


    


