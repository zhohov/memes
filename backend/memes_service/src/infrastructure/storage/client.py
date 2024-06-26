from typing import Any
import uuid
from datetime import timedelta
from minio import Minio
from minio.error import S3Error
from src.config import settings
from fastapi import UploadFile, HTTPException


def get_client() -> Minio:  
    client = Minio(
        endpoint=settings.storage.endpoint,
        access_key=settings.storage.access_key,
        secret_key=settings.storage.secret_key,
        secure=False,
    )

    return client


class StorageClient:
    def __init__(self) -> None:
        self._client: Minio = get_client()

    def _get_filename(self, filename: str) -> str:
        """Generate a unique filename using UUID."""

        return f"{uuid.uuid4()}{filename}"

    def _upload_file(self, file: UploadFile) -> str:
        """Upload a file to the Minio bucket."""

        filename: str = self._get_filename(filename=file.filename)

        self._client.put_object(
            bucket_name=settings.s3.minio_bucket,
            object_name=filename,
            data=file.file,
            length=-1, 
            part_size=10*1024*1024,
            content_type=file.content_type
        )

        return filename
    
    def _get_file_url(self, filename: str) -> str:
        """Get a presigned URL for the file in the Minio bucket."""

        try:
            self._client.stat_object(bucket_name=settings.s3.minio_bucket, object_name=filename)

            url: str = self._client.presigned_get_object(
                bucket_name=settings.s3.minio_bucket, 
                object_name=filename,
                expires=timedelta(seconds=8)
            )

            return url
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        