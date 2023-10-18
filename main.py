import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src import db_route

app = FastAPI()

@app.get("/")
async def is_alive():
    return RedirectResponse("/docs")

app.include_router(db_route.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8181)