import RPi.GPIO as GPIO
import time

BUTTON_PIN = 12
LED_GREEN = 15
LED_RED = 14


GPIO.setmode(GPIO.BCM)


GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)
try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            print("pressed")
            GPIO.output(LED_GREEN, GPIO.HIGH)
            GPIO.output(LED_RED, GPIO.LOW)
        else:
           
            GPIO.output(LED_GREEN, GPIO.LOW)
            GPIO.output(LED_RED, GPIO.HIGH)

        time.sleep(0.1) 
        
finally:
    GPIO.cleanup()
    
