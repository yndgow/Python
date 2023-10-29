from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi import FastAPI
import pandas_datareader.data as web
import datetime


# https://wikidocs.net/4766
start = datetime.datetime.now()
skhynix = web.DataReader('000660.KS', 'yahoo', start)


app = FastAPI()


@app.get("/")
def hello():
    return FileResponse('index.html')


@app.get("/data")
def hello():
    return {'hello': 123}


class userInfo(BaseModel):
    name: str
    phone: int


@app.post("/send")
def user(data: userInfo):
    print(data)
    return '수신완료'
