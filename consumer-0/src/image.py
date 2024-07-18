import pickle

import cv2
from PIL import Image

from .minio import get_minio_client, upload_image


def save_image(msg):
    data = pickle.loads(msg.value())

    print('Received message: input_type: {input_type}, received_at: {received_at}'.format(
        input_type=data["input_type"],
        received_at=data["received_at"],
    ))

    image = Image.fromarray(
        cv2.cvtColor(data["input"], cv2.COLOR_BGR2RGB)
    )

    topic_ref = 0
    image_name = data["input_type"] + "_flow_" + str(topic_ref) + "_" + data["received_at"].replace(" ", "_")
    images_path = "/"
    image_ext = ".png"

    bucket_name = 'images'
    client = get_minio_client(bucket_name)
    success = upload_image(
        client,
        bucket_name,
        images_path + image_name + image_ext,
        image
    )

    if success:
        print('Image saved in the bucket')
