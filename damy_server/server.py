# FastAPIの読み込み
from fastapi import FastAPI
from pydantic import BaseModel
import math

# FastAPIのインスタンスを作成
app = FastAPI()


@app.get("/data/getinfo")
async def getinfo():
    return {
        "temperature": 26.5,
        "humidity": 60,
        "isPeople": True,
        "lux": 77.4,
        "useairconditionaer": True,
        "airconditionaertime": "2024-06-30-22:20:50"
    }
