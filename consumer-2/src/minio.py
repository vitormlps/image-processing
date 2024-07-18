from io import BytesIO

from minio import Minio
from PIL import Image


def upload_image(client: Minio, bucket_name: str, file_full_name: str, source_file: Image.Image):
    # file = BytesIO(source_file)
    in_mem_file = BytesIO()
    source_file.save(in_mem_file, format='PNG')
    in_mem_file.seek(0)


    result = client.put_object(
        bucket_name=bucket_name,
        object_name=file_full_name,
        length=len(in_mem_file.getvalue()),
        data=in_mem_file,
    )

    return result.etag


def check_bucket(client: Minio, bucket_name: str):
    found = client.bucket_exists(bucket_name)

    if not found:
        client.make_bucket(bucket_name)


def get_minio_client(bucket_name):
    client = Minio(
        endpoint='minio:9000',
        access_key='minioadmin',
        secret_key='minioadmin',
        secure=False,
    )

    check_bucket(client, bucket_name)

    return client
