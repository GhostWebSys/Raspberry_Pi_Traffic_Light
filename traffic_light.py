import RPi.GPIO as GPIO
import time

RED_LIGHT = 18
YELLOW_LIGHT = 23
GREEN_LIGHT = 24

NOMAL_LIGHT_TIME = 10
WAIT_LIGHT_TIME = 3

def OffAllLight():
    # all off
    GPIO.output(RED_LIGHT,False)
    GPIO.output(YELLOW_LIGHT,False)
    GPIO.output(GREEN_LIGHT,False)  

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LIGHT,GPIO.OUT)    #red
GPIO.setup(YELLOW_LIGHT,GPIO.OUT) #yellow
GPIO.setup(GREEN_LIGHT,GPIO.OUT)  #green

OffAllLight()

# control
while(True):
    GPIO.output(YELLOW_LIGHT,False)
    GPIO.output(RED_LIGHT,True)
    time.sleep(NOMAL_LIGHT_TIME)

    GPIO.output(RED_LIGHT,False)
    GPIO.output(GREEN_LIGHT,True)
    time.sleep(NOMAL_LIGHT_TIME)

    GPIO.output(GREEN_LIGHT,False)
    GPIO.output(YELLOW_LIGHT,True)
    GPIO.output(RED_LIGHT,True)
    time.sleep(WAIT_LIGHT_TIME)

OffAllLight()

