import uvicorn
from fastapi import FastAPI

from config import settings
from infrastructure.application import create

app: FastAPI = create(title=settings.app_name, debug=settings.debug, routers=[])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
