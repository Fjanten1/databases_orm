from fastapi import FastAPI
from database import start_db
from routers import species, birds, birdspotting

app = FastAPI()

@app.on_event("startup")
def on_startup():
    start_db()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(species.router)
app.include_router(birds.router)
app.include_router(birdspotting.router)