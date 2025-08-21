from fastapi import FastAPI
from app.manager import Manager
import uvicorn

app = FastAPI()


# GET all hostile-tweets in db
@app.get("/hostile-tweets")
def get_all_tweet():

    return Manager().df_to_json()




if __name__ == '__main__':
    uvicorn.run(app,host="localhost",port=8000)