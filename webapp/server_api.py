from fastapi import FastAPI
import time

app = FastAPI()

logs = []

@app.post("/raw-data")
async def receive_raw_data(data: dict):
    start_time = time.time()
    # Simulate processing
    logs.append({
        "type": "raw",
        "size": len(str(data)),
        "timestamp": start_time
    })
    return {"status": "success", "latency": time.time() - start_time}

@app.get("/metrics")
async def get_metrics():
    return logs