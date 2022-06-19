import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
for i in range(10):
	GPIO.output(23, True)
	time.sleep(1)
	GPIO.output(23, False)
