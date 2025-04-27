import RPi.GPIO as GPIO
import time

R1 = 2
R2 = 3
R3 = 4
R4 = 17

C1 = 14
C2 = 15
C3 = 18
C4 = 23

#initialize
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
    if(GPIO.input(C1) == 1):
        print(characters[0])
    if(GPIO.input(C2) == 1):
        print(characters[1])
    if(GPIO.input(C3) == 1):
        print(characters[2])
    if(GPIO.input(C4) == 1):
        print(characters[3])
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        readLine(R1, ["1","2","3","A"])
        readLine(R2, ["4","5","6","B"])
        readLine(R3, ["7","8","9","C"])
        readLine(R4, ["*","0","#","D"])
        time.sleep(0.1)

except KeyboardInterrupt:
    print("stopped!")
