import uvicorn
from fastapi import FastAPI
from src import db_route

app = FastAPI()

@app.get("/")
async def is_alive():
    return {"message":"app is alive."}

app.include_router(db_route.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8181)