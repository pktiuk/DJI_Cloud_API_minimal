#!/usr/bin/env python3
import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

host_addr = os.environ["HOST_ADDR"]
username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

app = FastAPI()


@app.get("/login")
async def pilot_login():
    response = FileResponse("./couldhtml/login.html")
    response.body.replace("hostnamehere", host_addr)
    response.body.replace("userloginhere", username)
    response.body.replace("userpasswordhere", password)
    return response


if __name__ == "__main__":
    uvicorn.run(app, host=host_addr, port=5000)
