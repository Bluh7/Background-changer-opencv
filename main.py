import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from check_connected_webcams import check_connected_webcams
import os

webcam = 0
connected_webcams = check_connected_webcams(webcam)
cap = cv2.VideoCapture(webcam, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation(1)
fps_reader = cvzone.FPS()

valid_img = ["jpg", "png", "jpeg"]
img_path = os.listdir("images")
filtered_img_path = []

for img in img_path:
    if img.split(".")[-1] in valid_img:
        filtered_img_path.append(img)

img_list = []

for img in filtered_img_path:
    img = cv2.imread(f"images/{img}")
    img_list.append(img)

img_index = 0

while True:
    success, img = cap.read()
    img_out = segmentor.removeBG(img, img_list[img_index], threshold=0.59)

    img_stacked = cvzone.stackImages([img, img_out], 2, 1)
    fps, img_stacked = fps_reader.update(img_stacked, color=(0, 0, 255), scale=1.95)

    cv2.imshow("Image", img_stacked)
    key = cv2.waitKey(1)

    if key == ord("d"):
        if img_index < len(img_list) - 1:
            img_index += 1
    elif key == ord("a"):
        if img_index > 0:
            img_index -= 1
    elif key == ord("c"):
        if webcam < connected_webcams:
            webcam += 1
            cap = cv2.VideoCapture(webcam, cv2.CAP_DSHOW)
        elif webcam == connected_webcams:
            webcam = 0
            cap = cv2.VideoCapture(webcam, cv2.CAP_DSHOW)
    elif key == ord("q"):
        break
