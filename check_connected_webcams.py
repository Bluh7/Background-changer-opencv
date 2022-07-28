import cv2

def check_connected_webcams(webcam):
    while True:
        cap_check = cv2.VideoCapture(webcam, cv2.CAP_DSHOW)
        if cap_check.isOpened():
            webcam += 1
        elif cap_check is None or not cap_check.isOpened():
            break
    return webcam - 1