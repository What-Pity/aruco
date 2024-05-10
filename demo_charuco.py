import cv2
from aruco import charucoBoard
import numpy as np

bd = charucoBoard()
camera = cv2.VideoCapture(1)
intrinscis = np.genfromtxt(
    './camera_params/camera_matrix.csv', delimiter=',')
distortion = np.genfromtxt(
    './camera_params/distortion_coefficients.csv', delimiter=',')

while True:
    ret, frame = camera.read()
    if ret:
        charucoCorners, charucoIds, markerCorners, markerIds = bd.detect(frame)
        pose = None
        if charucoIds is not None and charucoIds.shape[0] > 6:
            pose = bd.pose_estimate(
                charucoCorners, charucoIds, intrinscis, distortion)
        frame = bd.draw(frame, charucoCorners, charucoIds,
                        pose, axis_size=1.5)
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key & 0xFF == 27:
            break


camera.release()
cv2.destroyAllWindows()
