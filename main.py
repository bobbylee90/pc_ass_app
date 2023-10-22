import time
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src import db_route
from src.helpers.dbconnector import MysqlConnector

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    time.sleep(3)
    with MysqlConnector() as conn:
        conn.create_tables()

@app.get("/")
async def is_alive():
    return RedirectResponse("/docs")

app.include_router(db_route.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8181)