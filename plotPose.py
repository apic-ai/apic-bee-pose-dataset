#!/usr/bin/env python3

import requests
import sys
import cv2
import json

from utils.imageUtils import numpyAsB64Png
from utils.drawPoseUtils import draw_keypoints

NN_INPUT_SIZE = (299, 299)

def load_image(image_path):
    return cv2.imread(image_path)

def load_label(labels_path, image_path):
    with open(labels_path) as json_file:
        data = json.load(json_file)
    for item in data:
        if item['path'] in image_path:
            return item
    return {}


def draw_result(image, result):
    print(result)
    pose_arr = []
    scale_x, scale_y, _ = image.shape
    scale_x /= NN_INPUT_SIZE[0]
    scale_y /= NN_INPUT_SIZE[1]
    confidence = 1
    for class_number, point in result["keypoints"].items():
        pose_arr.append([
            point[1] * scale_y,
            point[0] * scale_x,
            confidence,
            class_number
        ])
    image, kp_box = draw_keypoints(pose_arr, image, 0, 0)
    cv2.imshow("Bee pose image", image)
    cv2.waitKey(0)


def main(args):
    if len(args) > 1:
        image_path = args[0]
        labels_path = args[1]
        image = load_image(image_path)
        label = load_label(labels_path, image_path)
        draw_result(image, label)
    else:
        print("please add image path as argument")


if __name__ == "__main__":
    main(sys.argv[1:])
