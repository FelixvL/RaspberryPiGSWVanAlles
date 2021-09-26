import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(18, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(18, GPIO.LOW)

def ledje_laten_branden(pin):
	GPIO.output(pin, GPIO.HIGH)

def ledje_stoppen_branden(pin):
	GPIO.output(pin, GPIO.LOW)

led1 = 18
checkit = True
x = 0
while checkit:
	frequentie = GPIO.input(17)
	print("step: "+str(x)+" ingedrukt: "+str(frequentie))
	x = x+1
	if frequentie == 1 :
		ledje_laten_branden(led1)
	else:
		ledje_stoppen_branden(led1)
	time.sleep(0.05)
	if(x == 500):
		checkit = False




GPIO.cleanup()

