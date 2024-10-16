# FastAPIの読み込み
import random
from fastapi import FastAPI, Response

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
        "airconditioner_time": "2024-06-30-22:20:50"
    }


@app.get("/wifi/getinfo")
async def wifigetinfo():
    networks = []
    networks.append({"ssid": "MyWiFi", "signal_strength": "78"})
    networks.append({"ssid": "NeighborWiFi", "signal_strength": "54"})
    # print(json.dumps(networks))
    return networks


@app.get("/wifi/connect")
async def connect_wifi(ssid: str = None, password: str = None):
    if ssid == None or password == None:
        return Response(content="Bad Request: SSID and password required", status_code=400)

    if ssid == "MyWiFi" and password == "password":
        return {"status": "connected", "ssid": "MyWiFi"}

    return Response(content=f"Failed to connect to {ssid}: error occurred", status_code=500)
