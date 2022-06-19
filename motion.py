import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

try:
	while(True):
		GPIO.output(23, False)
		while(GPIO.input(18) == GPIO.HIGH):
			GPIO.output(23, True)
except KeyboardInterrupt:
	GPIO.cleanup()
		
