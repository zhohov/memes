from typing import List

from fastapi import APIRouter, File, Form, Request, UploadFile, status

from domain.memes import Meme, MemeCreate, memes_repository
from infrastructure.storage import client

memes_router = APIRouter(
    prefix="/memes",
    tags=["memes"],
)


@memes_router.get("/", status_code=status.HTTP_200_OK)
async def get(request: Request) -> List[Meme]:
    memes = await memes_repository._all()
    return memes


@memes_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_meme(
    request: Request, title: str = Form(...), file: UploadFile = File(...)
) -> Meme:
    filename = client._upload_file(file=file)
    meme = MemeCreate(title=title, image_name=filename)
    created_meme = await memes_repository._save(payload=meme.model_dump())

    return created_meme
