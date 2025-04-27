import cv2
import os

gst_pipeline = (
    "libcamerasrc ! "
    "video/x-raw,width=640,height=480,format=RGB888 ! "
    "videoconvert ! "
    "appsink"
)

cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

ret, frame = cap.read()

if ret:
    cv2.imwrite('facesFolder/snapshot.jpg', frame)
    print("succeedded")
else:
    print("failed")

cap.release()
