import cv2
from aruco import aruco
import numpy as np

bd = aruco()
camera = cv2.VideoCapture(0)
intrinscis = np.genfromtxt(
    './camera_params/camera_matrix.csv', delimiter=',')
distortion = np.genfromtxt(
    './camera_params/distortion_coefficients.csv', delimiter=',')

while True:
    ret, frame = camera.read()
    if ret:
        corners, ids, rejectedImgPoints = bd.detect(frame)
        pose = bd.pose_estimate(corners, intrinscis, distortion)
        frame = bd.draw(frame, corners, ids, pose, 1.5)
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key & 0xFF == 27:
            break


camera.release()
cv2.destroyAllWindows()
