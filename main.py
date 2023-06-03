# import boto3
# import uvicorn
from fastapi import FastAPI
from api.glueapi import router 
from api.s3api import s3router

app = FastAPI()

app.include_router(prefix="/api/v1", router=router)
app.include_router(prefix="/api/v1", router=s3router)

@app.get('/', status_code=200)
def health_check():
    return {"message": "Ok"}

# if __name__ == "__main__":
#     uvicorn.run(api, host="127.0.0.1", port=8000)
