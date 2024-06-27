from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from .base import Base


class IdMixin:
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )


class MemesTable(Base, IdMixin, TimestampMixin):
    __tablename__ = "memes"

    title: Mapped[str] = mapped_column(nullable=False)
    image_name: Mapped[str] = mapped_column(nullable=False)
