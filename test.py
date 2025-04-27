import cv2

gst_pipeline = (
    "libcamerasrc ! "
    "video/x-raw,width=640,height=480,format=RGB888 ! "
    "videoconvert ! "
    "appsink"
)

cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

ret, frame = cap.read()

if ret:
    cv2.imwrite('snapshot.jpg', frame)
    print("✅ Image captured!")
else:
    print("❌ Failed to capture image.")

cap.release()
