#!/usr/bin/env python3

import base64
from PIL import Image
import cv2
from io import BytesIO
import numpy as np

IMAGE_PREFIX = 'base64,'
PNG_B64_PREFIX = 'data:image/png;base64,'
JPEG_B64_PREFIX = 'data:image/jpeg;base64,'


def b64ToNumpy(base64_string):
    if IMAGE_PREFIX in base64_string:
        base64_string = base64_string.split(IMAGE_PREFIX, 1)[1]
    img_data = base64.b64decode(base64_string)
    pil_image = Image.open(BytesIO(img_data))
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)


def numpyAsB64Png(frame):
    # print("data type: " + str(frame.dtype) + " max: " + str(frame.max()))
    _, buffer = cv2.imencode('.png', frame)
    png_as_text = base64.b64encode(buffer).decode("utf-8")
    return PNG_B64_PREFIX + png_as_text


def numpyAsB64Jpg(frame):
    # print("data type: " + str(frame.dtype) + " max: " + str(frame.max()))
    _, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = base64.b64encode(buffer).decode("utf-8")
    return JPEG_B64_PREFIX + jpg_as_text
