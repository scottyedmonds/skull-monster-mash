# Test of Servo movement for Skull
# Need PWM board to translate sound into jaw movement

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT) #set pin to num. 12 which is GPIO18 on RPi3

servo = GPIO.PWM(12, 50) # Define GPIO.PWM to pin num. 12 @ 50hz (i think it's hertz?)

pos = 4.0 # beginning position of servo
x = 3 # multiplier used

servo.start(4.0)

try:
	while True:
	# For statement example
		for pos in range(3, int(x*pos)):
			pos = pos / 10.0 + 3
			servo.ChangeDutyCycle(pos)
			print(pos)
			time.sleep(0.25)

		for pos in range(20, int(x*pos), -1):
			pos = pos / 10 + 3
			servo.ChangeDutyCycle(pos)
			print(pos)
			time.sleep(0.25)
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
