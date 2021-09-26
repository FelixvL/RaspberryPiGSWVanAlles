import RPi.GPIO as GPIO
import time

print('hoi')

time.sleep(3)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)

frequentie = GPIO.input(18)
print('hoihoi')

f = open('test', 'r')
print(f.read())

x = f.readline()
print(x)

f.close()

f = open('test', 'a')
f.write("joepie een derde zin")
f.close()