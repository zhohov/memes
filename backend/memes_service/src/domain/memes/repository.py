from typing import List

from infrastructure.database import BaseRepository, MemesTable

from .models import Meme


class MemesRepository(BaseRepository[MemesTable]):
    _schema_class = MemesTable

    async def get_all(self) -> List[Meme]:
        memes = await self._all()
        return memes

    async def get_by_id(self, id: int) -> Meme:
        meme = await self._get(key="id", value=id)
        return meme


memes_repository = MemesRepository()
