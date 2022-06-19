import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
try:
	while(True):
		GPIO.output(23, False)
		while(GPIO.input(4) == GPIO.LOW):
			GPIO.output(23, True)
except KeyboardInterrupt:
	GPIO.cleanup()
		
