import RPi.GPIO as GPIO
from time import sleep
''' Pin Setup
led 1 = GPIO17
led 2 = GPIO27
led 3 = GPIO18
button1 = GPIO22
button2 = GPIO23 '''

# LED 3 Constant Blinking:
GPIO.setmode(GPIO.BCM) 
p3 = 18 # 3rd LED pin #
GPIO.setup(p3, GPIO.OUT) # Assign pin as output

while True:
  GPIO.output(p3, 0)
  sleep(0.5)
  GPIO.output(p3, 1)
  sleep(0.89)