from pydantic import Field
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    db_name: str = Field(..., env="DB_NAME")
    db_user: str = Field(..., env="DB_USER")
    db_password: str = Field(..., env="DB_PASSWORD")
    db_host: str = Field(..., env="DB_HOST")
    db_port: int = Field(..., env="DB_PORT")

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"  # noqa: E501


class StorageSettings(BaseSettings):
    endpoint: str = Field(..., env="MINIO_ENDPOINT")
    access_key: str = Field(..., env="MINIO_ACCESS_KEY")
    secret_key: str = Field(..., env="MINIO_SECRET_KEY")
    bucket_name: str = Field(..., env="MINIO_BUCKET_NAME")
    secure: bool = Field(default=False, env="MINIO_SECURE")


class Settings(BaseSettings):
    app_name: str = Field(default="FastAPI", env="TITLE")
    debug: bool = Field(default=True, env="DEBUG")

    database: DatabaseSettings = DatabaseSettings()
    storage: StorageSettings = StorageSettings()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings: Settings = Settings()
