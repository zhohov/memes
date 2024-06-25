from pydantic import Field
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    ...


class Settings(BaseSettings):
    app_name: str = Field(default="FastAPI", env="TITLE")
    debug: bool = Field(default=True, env="DEBUG")

    database: DatabaseSettings  = DatabaseSettings()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings: Settings = Settings()
