import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

redflag = 0
yellowflag = 0
greenflag = 0

while(1) :
	answer = input("\n enter menu : ")
	print("\n the answer was ", answer)

	if answer == 1 :
		if yellowflag == 0 :
			GPIO.setup(11, GPIO.OUT)
			GPIO.output(11, GPIO.HIGH)
			yellowflag = 1
		else :
			GPIO.output(11, GPIO.LOW)
			yellowflag = 0
	elif answer == 2 :
		if redflag == 0 :
			GPIO.setup(13, GPIO.OUT)
			GPIO.output(13, GPIO.HIGH)
			redflag = 1
		else :
			GPIO.output(13, GPIO.LOW)
			redflag = 0
	elif answer == 3 :
		if greenflag == 0 :
			GPIO.setup(15, GPIO.OUT)
			GPIO.output(15, GPIO.HIGH)
			greenflag = 1
		else :
			GPIO.output(15, GPIO.LOW)
			greenflag = 0
	else :
		GPIO.cleanup(11)
		GPIO.cleanup(13)
		GPIO.cleanup(15)
		redflag = 0
		yellowflag = 0
		greenflag = 0
		GPIO.cleanup()
		exit()
