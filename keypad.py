import RPi.GPIO as GPIO
import time
import face  

R1 = 2
R2 = 3
R3 = 4
R4 = 17

C1 = 14
C2 = 15
C3 = 18
C4 = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(R3, GPIO.OUT)
GPIO.setup(R4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if GPIO.input(C1) == 1:
        return characters[0]
    if GPIO.input(C2) == 1:
        return characters[1]
    if GPIO.input(C3) == 1:
        return characters[2]
    if GPIO.input(C4) == 1:
        return characters[3]
    GPIO.output(line, GPIO.LOW)
    return None

password = "1234"
def readKeys():
    keys = []
    for i in range(4):
        key_detected = False
        while not key_detected:
            key = readLine(R1, ["1", "2", "3", "A"]) or \
                  readLine(R2, ["4", "5", "6", "B"]) or \
                  readLine(R3, ["7", "8", "9", "C"]) or \
                  readLine(R4, ["*", "0", "#", "D"])

            if key is not None:
                print(f"Key pressed: {key}")
                keys.append(key)
                key_detected = True  # Key detected, move to the next key
            time.sleep(0.1)  # Debounce time
    return keys

while True:
    temp = readKeys()
        if temp == password:
            print("Password correct")
            if readKeys() == "0000":
                print("new password")
                password = readKeys()
            if readKeys() == "####":
                print("new face:")
                face.addFace(input("Enter ID: "))
        elif temp == "####":  
            if face.runFacialRecognition():
                print("accessed")
            else:
                print("access denied")
        else:
            print("Password incorrect")
            temp = "" 
            time.sleep(1) 
