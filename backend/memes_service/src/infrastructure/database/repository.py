from typing import TypeVar, Generic, Any
from sqlalchemy import Result, asc, delete, desc, func, select, update

from .session import Session
from .base import Base

T = TypeVar("T", bound=Base)


class BaseRepository(Session, Generic[T]):
    _schema_class: type[T]

    def __init__(self) -> None:
        super().__init__()

        if not self._schema_class:
            raise Exception("schema_class is not set")
        
    async def _get(self, key: str, value: Any) -> T:
        query = select(self.schema_class).where(
            getattr(self.schema_class, key) == value
        )
        result: Result = await self.execute(query)

        if not (_result := result.scalars().one_or_none()):
            raise Exception(f'No result found for key:  {key} and value: {value}')
        
        return  _result
    
    async def _all(self)  -> list[T]:
        query = select(self.schema_class)
        result: Result  = await self._session.execute(query)
        return  result.scalars().all()
        
    async def _save(self, payload: dict[str, Any]) -> T:
        try: 
            schema = self.schema_class(**payload)
            self._session.add(schema)
            await self._session.flush()
            await self._session.refresh()
            return schema
        except self._ERRORS:
            raise 
