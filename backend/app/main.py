from fastapi import FastAPI

app = FastAPI(title="Platform Core")

@app.get("/")
def root():
    return {"status": "ok", "service": "platform-core"}
