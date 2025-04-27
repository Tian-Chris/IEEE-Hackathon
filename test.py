import cv2
 
 cap = cv2.VideoCapture(0)
 cap.read()
 ret, frame = cap.read()
 
 if ret:
     cv2.imwrite("snapshot.jpg", frame)
     print("photo captured successfully.")
 else:
     print("failed to capture image.")
 
 cap.release()