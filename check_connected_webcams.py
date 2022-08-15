import cv2
import os

def check_connected_webcams(webcam):
    while True:
        if os.name == "nt":
            cap_check = cv2.VideoCapture(webcam, cv2.CAP_DSHOW)
        else:
            cat_check = cv2.VideoCapture(webcam)
        if cap_check.isOpened():
            webcam += 1
        elif cap_check is None or not cap_check.isOpened():
            break
    return webcam - 1
