from fastapi import FastAPI

app = FastAPI(title="Wildfire Monitoring API")

@app.get("/")
def health_check():
    return {"status": "ok", "service": "wildfire-backend"}
