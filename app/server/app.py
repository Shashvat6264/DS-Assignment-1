from fastapi import FastAPI

app = FastAPI()

@app.get("/health", tags=["HEALTH"])
async def health():
    return {"message": "Server Running Successfully..."}