#!/usr/bin/env python3

#############
# Keypoints #
#############

head_color = (0, 0, 255)
body_color = (255, 0, 0)
wing_color = (0, 255, 0)
left_leg_color = (0, 255, 255)
right_leg_color = (255, 255, 0)

label_to_keypoint = {"0": {"name": "head_front", "color": head_color},
                     "1": {"name": "head_left", "color": head_color},
                     "2": {"name": "head_right", "color": head_color},
                     "3": {"name": "head_back", "color": body_color},
                     "4": {"name": "body_center", "color": body_color},
                     "5": {"name": "body_back", "color": body_color},
                     "6": {"name": "wing_left", "color": wing_color},
                     "7": {"name": "wing_right", "color": wing_color},
                     "8": {"name": "right_leg_front_1", "color": right_leg_color},
                     "9": {"name": "right_leg_front_2", "color": right_leg_color},
                     "10": {"name": "right_leg_front_3", "color": right_leg_color},
                     "11": {"name": "right_leg_front_4", "color": right_leg_color},
                     "12": {"name": "right_leg_middle_1", "color": right_leg_color},
                     "13": {"name": "right_leg_middle_2", "color": right_leg_color},
                     "14": {"name": "right_leg_middle_3", "color": right_leg_color},
                     "15": {"name": "right_leg_middle_4", "color": right_leg_color},
                     "16": {"name": "right_leg_back_1", "color": right_leg_color},
                     "17": {"name": "right_leg_back_2", "color": right_leg_color},
                     "18": {"name": "right_leg_back_3", "color": right_leg_color},
                     "19": {"name": "right_leg_back_4", "color": right_leg_color},
                     "20": {"name": "left_leg_front_1", "color": left_leg_color},
                     "21": {"name": "left_leg_front_2", "color": left_leg_color},
                     "22": {"name": "left_leg_front_3", "color": left_leg_color},
                     "23": {"name": "left_leg_front_4", "color": left_leg_color},
                     "24": {"name": "left_leg_middle_1", "color": left_leg_color},
                     "25": {"name": "left_leg_middle_2", "color": left_leg_color},
                     "26": {"name": "left_leg_middle_3", "color": left_leg_color},
                     "27": {"name": "left_leg_middle_4", "color": left_leg_color},
                     "28": {"name": "left_leg_back_1", "color": left_leg_color},
                     "29": {"name": "left_leg_back_2", "color": left_leg_color},
                     "30": {"name": "left_leg_back_3", "color": left_leg_color},
                     "31": {"name": "left_leg_back_4", "color": left_leg_color}
                     }
connections = [["head_front", "head_left", head_color, 50],
               ["head_front", "head_right", head_color, 50],
               ["head_front", "head_back", body_color, 50],
               ["head_back", "body_center", body_color, 80],
               ["body_center", "body_back", body_color, 200],
               ["wing_left", "head_back", wing_color, 200],
               ["wing_right", "head_back", wing_color, 200],
               ["right_leg_front_1", "right_leg_front_2", right_leg_color, 40],
               ["right_leg_front_2", "right_leg_front_3", right_leg_color, 40],
               ["right_leg_front_3", "right_leg_front_4", right_leg_color, 60],
               ["right_leg_middle_1", "right_leg_middle_2", right_leg_color, 50],
               ["right_leg_middle_2", "right_leg_middle_3", right_leg_color, 50],
               ["right_leg_middle_3", "right_leg_middle_4", right_leg_color, 70],
               ["right_leg_back_1", "right_leg_back_2", right_leg_color, 60],
               ["right_leg_back_2", "right_leg_back_3", right_leg_color, 60],
               ["right_leg_back_3", "right_leg_back_4", right_leg_color, 80],
               ["left_leg_front_1", "left_leg_front_2", left_leg_color, 40],
               ["left_leg_front_2", "left_leg_front_3", left_leg_color, 40],
               ["left_leg_front_3", "left_leg_front_4", left_leg_color, 60],
               ["left_leg_middle_1", "left_leg_middle_2", left_leg_color, 50],
               ["left_leg_middle_2", "left_leg_middle_3", left_leg_color, 50],
               ["left_leg_middle_3", "left_leg_middle_4", left_leg_color, 70],
               ["left_leg_back_1", "left_leg_back_2", left_leg_color, 60],
               ["left_leg_back_2", "left_leg_back_3", left_leg_color, 60],
               ["left_leg_back_3", "left_leg_back_4", left_leg_color, 80]]
