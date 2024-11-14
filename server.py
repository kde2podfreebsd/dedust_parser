from fastapi import FastAPI, status, Query
from pydantic import BaseModel
import json
import uvicorn

app = FastAPI()

print("kek")

@app.get("/all_pools", tags=["dedust"])
def get_all_pools():
    with open("pool_data.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/pool_info", tags=["dedust"])
def get_pool_info(pool_name: str = Query(...)):
    with open("pool_data.json", "r") as file:
        data = json.load(file)
    for pool in data[0]["pools"]:
        if pool["name"] == pool_name:
            return {"timestamp": data[0]["timestamp"], "pool_info": pool}
    return {"error": "Pool not found"}

class HealthCheck(BaseModel):
    status: str = "OK"

@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
)
def get_health() -> HealthCheck:
    return HealthCheck(status="OK")


#if __name__ == "__main__":
#    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=False, log_level="debug",
#                workers=1, limit_concurrency=1, limit_max_requests=1)
