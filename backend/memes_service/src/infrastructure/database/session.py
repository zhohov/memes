from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker, AsyncEngine
from contextvars import ContextVar
from sqlalchemy import Result
from sqlalchemy.exc import IntegrityError, PendingRollbackError
from config import settings

engine: AsyncEngine = create_async_engine(
    url=settings.database.url, echo=True
)


def get_async_session(engine: AsyncEngine | None = engine) -> AsyncSession:
    Session: async_sessionmaker = async_sessionmaker(
        bind=engine, expire_on_commit=False,
    )

    return Session()

CTX_SESSION: ContextVar[Optional[AsyncSession]] = ContextVar(
    name="session", default=get_async_session()
)


class Session:
    _ERRORS = (IntegrityError, PendingRollbackError)

    def __init__(self) -> None:
        self._session: Optional[AsyncSession] = CTX_SESSION.get()

        if self._session is None:
            raise RuntimeError("Session not initialized.")
    
    async def execute(self, query: str) -> Result:
        try:
            result = await self._session.execute(query)
            return result
        except self._ERRORS:
            raise
