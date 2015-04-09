import RPi.GPIO as GPIO
import time

MOTION = 13 #pin 13 used for motion detector

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(MOTION, GPIO.IN)


var = 1

def main():
	#main function where we wait for touch input

	while var == 1:
		if GPIO.input(MOTION)==GPIO.HIGH:
			#for testing
			#print "Movement detected!"

			twitter()

		else:
			print "No movement"

		time.sleep(1)
		#will be used if no sleep causes problems

def twitter():
	#function that is called when touch is detected
	#here we parse the file containing our twitter api information
	#and gather information we want to post
	#and pass them into post() function


	return


main()
