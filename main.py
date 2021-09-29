import RPi.GPIO as GPIO

from time import sleep
''' Pin Setup
led 1 = GPIO17
led 2 = GPIO27
led 3 = GPIO18
button1 = GPIO22
button2 = GPIO23 '''
GPIO.setmode(GPIO.BCM) 

# Pin Numbers:
p1 = 17 # 1st LED pin 
p2 = 27 # 2nd LED pin
p3 = 18 # 3rd LED pin 
i1 = 22 # Button 1
i2 = 23 # Button 2 

GPIO.setup(p1, GPIO.OUT) # Assign LED 1 output pin
GPIO.setup(p2, GPIO.OUT) # Assign LED 2 output pin
GPIO.setup(p3, GPIO.OUT) # Assign LED 3 output pin

# Initial conditions:
GPIO.output(p1, 0)
GPIO.output(p2, 0)
GPIO.setup(i1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(i2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED 1 threaded callback function:
def myCallback(i1):
  # Put code here
    GPIO.output(p1, 1)
    sleep(0.5)
    GPIO.output(p1, 0)
    sleep(0.5)

# LED 2 threaded callback function:
def myCallback2(i2):
    GPIO.output(p2, 1)
    sleep(0.5)
    GPIO.output(p2, 0)
    sleep(0.5)

GPIO.add_event_detect(i1, GPIO.RISING, callback= myCallback, bouncetime=100)

GPIO.add_event_detect(i2, GPIO.RISING, callback= myCallback2, bouncetime=100)

# LED 3 Constant Blinking:
try:
  while True:
    GPIO.output(p3, 0)
    sleep(0.5)
    GPIO.output(p3, 1)
    sleep(0.5)
  

# Exception Handling for exiting program smoothly:
except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e:
  print('\ne')
GPIO.cleanup()