from aruco import aruco, arucoBoard, charucoBoard, charucoDiamond
import cv2

charuco = charucoBoard()
charuco_img = charuco.generate()
cv2.imshow("Charuco", charuco_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("charuco.png", charuco_img)
