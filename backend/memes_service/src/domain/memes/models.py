from datetime import datetime

from pydantic import BaseModel


class MemeCreate(BaseModel):
    title: str
    image_name: str


class Meme(BaseModel):
    id: int
    title: str
    image_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
