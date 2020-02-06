from PIL import ImageFont, ImageDraw
import cv2
import hashlib
import numpy as np
import os
import shutil

from utils.definitions import label_to_keypoint, connections

def get_color(identifier):
    hash_string = str(hashlib.sha384(
        str(identifier).encode('utf-8')).hexdigest())
    hex_list = list(map(''.join, zip(*[iter(hash_string)] * 2)))[-3:]
    rgb_list = []
    for component in hex_list:
        rgb_list.append(int(component, base=16))
    return tuple(rgb_list)


def draw_keypoints(pks_pred, image, offset_x, offset_y):
    centers = {}
    x_min = 10000
    x_max = 0
    y_min = 10000
    y_max = 0
    for i, pred in enumerate(pks_pred):
        if i == 0:
            print("head_pred", pred)
        pk_y, pk_x, conf_value, ind = pred
        padding = 10
        if padding <= pk_y <= 299 - padding and padding <= pk_x <= 299 - padding and conf_value > 0.4:
            x_min = int(min(x_min, pk_x + offset_x))
            x_max = int(max(x_max, pk_x + offset_x))
            y_min = int(min(y_min, pk_y + offset_y))
            y_max = int(max(y_max, pk_y + offset_y))
            v = label_to_keypoint[str(int(ind))]
            center = (int(pk_x + offset_x), int(pk_y + offset_y))
            centers[v["name"]] = center
            cv2.circle(image, center, 2, v["color"],
                       thickness=2, lineType=8, shift=0)
            label_str = str(round(conf_value, 2))  # v["name"] + "_" +
            #cv2.putText(image, label_str, (center[0] + 5, center[1]), 0, 0.5, v["color"], 1, cv2.LINE_AA)

    # lines
    for pair_order, pair in enumerate(connections):
        if pair[0] in centers and pair[1] in centers:
            dist = eukl_dist(centers[pair[0]], centers[pair[1]])
            if dist < pair[3]:
                cv2.line(image, centers[pair[0]],
                         centers[pair[1]], pair[2], thickness=2)

    #cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (30,30,30), thickness=1)
    kp_box = [x_min, y_min, x_max, y_max]
    return image, kp_box


def eukl_dist(pk_1, pk_2):
    distance_x = np.abs(pk_1[0] - pk_2[0])
    distance_y = np.abs(pk_1[1] - pk_2[1])
    return np.sqrt(np.square(distance_x) + np.square(distance_y))
