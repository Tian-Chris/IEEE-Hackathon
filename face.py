import cv2
import requests
import os

API_KEY = input("Enter API : ").strip()
ENDPOINT = 'https://hackaiface.cognitiveservices.azure.com/'

detect_url = ENDPOINT + "/face/v1.0/detect"
verify_url = ENDPOINT + "/face/v1.0/verify"

headers = {
    'Ocp-Apim-Subscription-Key': API_KEY,
    'Content-Type': 'application/octet-stream'
}
params_detect = {
    'returnFaceId': 'true'
}

gst_pipeline = (
    "libcamerasrc ! "
    "video/x-raw,width=640,height=480,format=RGB888 ! "
    "videoconvert ! "
    "appsink"
)

def detectFace(image_path):
    with open(image_path, 'rb') as f:
        data = f.read()
    faces = requests.post(detect_url, params=params_detect, headers=headers, data=data).json()
    if faces:
        return faces[0]['faceId']
    return

def checkSame(face_id1, face_id2):
    body = {
        "faceId1": face_id1,
        "faceId2": face_id2
    }
    result = requests.post(verify_url, headers=headers, json=body).json()
    return result['isIdentical'], result['confidence']

cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)
ret, frame = cap.read()
if ret:
    cv2.imwrite('snapshot.jpg', frame)
else:
    print("Failed to capture image.")
    exit()
cap.release()

detectedFace = detectFace('snapshot.jpg')
if detectedFace is None:
    print("No face detected.")
    exit()


for filename in os.listdir(facesFolder):
    if filename.lower().endswith(('.jpg')):
        id = detectFace(os.path.join(facesFolder, filename))
        if id is None:
            print(f"No detected in {filename}")
            continue
        identical, confidence = checkSame(detectedFace, id)
        print(f"{filename}; identical: {identical}, Confidence: {confidence:.2f})")
        if identical:
            print(f" face found: {filename}!")
            break
print("No match")
