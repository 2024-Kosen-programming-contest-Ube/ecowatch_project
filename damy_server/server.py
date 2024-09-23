# FastAPIの読み込み
import random
from fastapi import FastAPI
from pydantic import BaseModel
import math

# FastAPIのインスタンスを作成
app = FastAPI()


@app.get("/data/getinfo")
async def getinfo():
    # return {
    #     "temperature": 26.5,
    #     "humidity": 60,
    #     "isPeople": True,
    #     "lux": 77.4,
    #     "useairconditionaer": True,
    #     "airconditionaertime": "2024-06-30-22:20:50"
    # }
    return {
        "temperature": random.randint(20, 40),
        "humidity": random.randint(50, 100),
        "isPeople": True,
        "lux": 77.4,
        "useairconditioner": True,
        "airconditionaer_time": "2024-06-30-22:20:50"
    }
