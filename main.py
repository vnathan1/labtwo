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

GPIO.setup(p3, GPIO.OUT) # Assign LED 3 output pin
GPIO.setup(i1, GPIO.IN, wave=GPIO.wave)
GPIO.setip(i2, GPIO.IN, wave=GPIO.wave)

#Thread callback function:
def wave1(i1):
  # Put code here
  return
def wave2(i2):
  return

GPIO.add_event_detect(i1, GPIO.RISING, callback= wave1, bouncetime=100)

GPIO.add_event_detect(i2, GPIO.RISING, callback= wave2, bouncetime=100)

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