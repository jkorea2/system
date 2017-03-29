import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, GPIO.LOW)


def gotit(channel):
	print("Got it", channel)

GPIO.add_event_detect(5, GPIO.RISING, callback=gotit, bouncetime=300)

time.sleep(3)
GPIO.output(3, GPIO.HIGH)

start_time = time.time()


while True:

	v = GPIO.input(5)

	if v is not 0:
		end_time = time.time()
		print(end_time - start_time)
		GPIO.output(3, GPIO.LOW)
		exit()

	time.sleep(1)

GPIO.cleanup()
