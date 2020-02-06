#!/usr/bin/env python3

import requests
import sys
import cv2

sys.path.append('../utils')

from utils.imageUtils import numpyAsB64Png
from utils.drawPoseUtils import draw_keypoints

NN_INPUT_SIZE = (240, 240)

def load_image(image_path):
    return cv2.imread(image_path)


def draw_result(image, result):
    pose_arr = []
    scale_x, scale_y, _ = image.shape
    scale_x /= NN_INPUT_SIZE[0]
    scale_y /= NN_INPUT_SIZE[1]
    for point in result["pose"]:
        pose_arr.append([
            point['position']['y'] * scale_y,
            point['position']['x'] * scale_x,
            point["conf"],
            point["class_number"]
        ])
    image, kp_box = draw_keypoints(pose_arr, image, 0, 0)
    cv2.imshow("Bee pose image", image)
    cv2.waitKey(0)


def main(args):
    if len(args) > 1:
        image_path = args[0]
        label_path = args[1]
        image = load_image(image_path)
        label = load_label(label_path)
        draw_result(image, label)
    else:
        print("please add image path as argument")


if __name__ == "__main__":
    main(sys.argv[1:])
