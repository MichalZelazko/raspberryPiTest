"""import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

try:
	while(True):
		GPIO.output(23, False)
		time.sleep(0.1)
		print("nie widze")
		if(GPIO.input(18) == GPIO.HIGH):
			GPIO.output(23, True)
			print("widze")
			time.sleep(0.1)
			
except KeyboardInterrupt:
	GPIO.cleanup()
		"""
		
from gpiozero import MotionSensor

pir = motionsensor(18)

while True:
	pir.wait_for_motion()
	print("you moved")
	pir.wait_for_no_motion()
