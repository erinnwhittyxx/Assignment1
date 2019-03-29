from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)

while True:
	for i in range(3): 
		GPIO.output(22, GPIO.HIGH)
		sleep(0.25)
		GPIO.output(22, GPIO.LOW)
		sleep(0.25)

	for i in range(3):
		GPIO.output(22, GPIO.HIGH)
		sleep(0.5)
		GPIO.output(22, GPIO.LOW)
		sleep(0.5)

	for i in range(3): 
		GPIO.output(22, GPIO.HIGH)
		sleep(0.25)
		GPIO.output(22, GPIO.LOW)
		sleep(0.25)

	sleep(1)
	

	
