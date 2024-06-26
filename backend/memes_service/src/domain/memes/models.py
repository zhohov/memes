from datetime import datetime

from pydantic import BaseModel


class MemeCreate(BaseModel):
    title: str
    image_url: str


class Meme(BaseModel):
    id: int
    title: str
    image_url: str
    created_at: datetime.timestamp
    updated_at: datetime.timestamp

    class Config:
        from_attributes = True