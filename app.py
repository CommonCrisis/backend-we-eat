import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from backend_we_eat.routers.v1 import recepies

load_dotenv()

app = FastAPI()

app.include_router(recepies.router)


uvicorn.run(app)
