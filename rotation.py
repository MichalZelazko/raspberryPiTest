import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(4, GPIO.IN)

count = 0

try:
	while(True):
		start = time.perf_counter_ns()
		GPIO.output(23, False)
		if(GPIO.input(2) == GPIO.HIGH):
			right = time.perf_counter_ns()
			left = time.perf_counter_ns()
		if(GPIO.input(3) == GPIO.HIGH):
			right = time.perf_counter_ns()
			left = time.perf_counter_ns()
		if(right-left>0):
			count = count - 1
			print(count)
		else:
			count = count + 1
			print(count)
		while(GPIO.input(4) == GPIO.LOW):
			GPIO.output(23, True)
except KeyboardInterrupt:
	GPIO.cleanup()
		
