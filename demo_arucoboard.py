import cv2
from aruco import arucoBoard
import numpy as np

bd = arucoBoard()
camera = cv2.VideoCapture(1)
intrinscis = np.genfromtxt(
    './camera_params/camera_matrix.csv', delimiter=',')
distortion = np.genfromtxt(
    './camera_params/distortion_coefficients.csv', delimiter=',')

while True:
    ret, frame = camera.read()
    if ret:
        corners, ids, rejectedImgPoints = bd.detect(frame)
        pose = None
        if ids is not None:
            pose = bd.pose_estimate(corners, ids, intrinscis, distortion)
        frame = bd.draw(frame, corners, ids, pose, 1.5)
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key & 0xFF == 27:
            break


camera.release()
cv2.destroyAllWindows()
