from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

while True:
	for i in range(3): 
		GPIO.output(17, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		sleep(0.5)
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		sleep(0.5)

	for i in range(3):
		GPIO.output(17, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		sleep(0.25)
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		sleep(0.25)

	for i in range(3): 
		GPIO.output(17, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		sleep(0.5)
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		sleep(0.5)

	sleep(1)
	

	