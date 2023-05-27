import boto3
import uvicorn
from fastapi import FastAPI
from app.glueapi import router
app = FastAPI()


app.include_router(prefix="/api/v1",router=router)
@app.get('/',status_code=200)
def health_check():
    return {"message": "Ok"}



# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)