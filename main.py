# Vivek Nathan
# Lab 2 Code 

import RPi.GPIO as GPIO # Import RPi.GPIO module

from time import sleep # For LED 3 Constant Blinking
GPIO.setmode(GPIO.BCM) # BCM port numbering

# All Pin Numbers:
p1 = 17 # 1st LED pin 
p2 = 27 # 2nd LED pin
p3 = 18 # 3rd LED pin 
i1 = 22 # Button 1 Input pin
i2 = 23 # Button 2 Input pin

GPIO.setup(p1, GPIO.OUT) # Assign LED 1 output pin
GPIO.setup(p2, GPIO.OUT) # Assign LED 2 output pin
GPIO.setup(p3, GPIO.OUT) # Assign LED 3 output pin

# Threaded callback setup for LED 1 & LED 2
GPIO.setup(i1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(i2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED 1 PWM object 
pwm1 = GPIO.PWM(p1,100)
# LED 2 PWM object 
pwm2 = GPIO.PWM(p2,100)

# LED 1 Threaded Callback function for i1 (pin GPIO22):
def myCallback(i1):
    pwm1.start(0) # Start PWM cycle at 0% duty cycle
    for dc in range(0,100,1): # Iterate PWM from 0 to 100 in increments of 1
      pwm1.ChangeDutyCycle(dc) # Set duty cycle for off to on
      sleep(0.005) # Sleep 5 ms (With this value, the total time of the wave cycle is 1 second, therefore it is a 1 Hz Cycle) 
    for dc in range(100,-1,-1): # Iterate PWM back to 0 in increments of 1
      pwm1.ChangeDutyCycle(dc) # Set duty cycle for on to off
      sleep(0.005) # Sleep 5 ms (With this value, the total time of the wave cycle is 1 second, therefore it is a 1 Hz Cycle) 

# LED 2 threaded callback function for i2 (pin GPIO23): *** Identical function
def myCallback2(i2): 
    pwm2.start(0)
    for dc in range(0,100,1):
      pwm2.ChangeDutyCycle(dc)
      sleep(0.005)
    for dc in range(100,-1,-1):
      pwm2.ChangeDutyCycle(dc)
      sleep(0.005)

# Execute LED 1 threaded callback function if i1 (pin GPIO22) goes HIGH
GPIO.add_event_detect(i1, GPIO.RISING, callback= myCallback, bouncetime=100)
# Execute LED 2 threaded callback function if i2 (pin GPIO23) goes HIGH
GPIO.add_event_detect(i2, GPIO.RISING, callback= myCallback2, bouncetime=100)

# LED 3 Constant Blinking:
try:
  while True: # Loop runs continuously
    GPIO.output(p3, 1) # Sets LED 3 (pin GPIO18) to 3.3 Volts
    sleep(0.5) # Waits 0.5 seconds (Totals to 1 second, i.e. 1 Hz)
    GPIO.output(p3, 0) # Sets LED 3 (pin GPIO18) to 0 Volts
    sleep(0.5)# Waits 0.5 seconds (Totals to 1 second, i.e. 1 Hz)
  
# Exception Handling for exiting program smoothly:
except KeyboardInterrupt: # if user hits Ctrl-C
  print('\nExiting')
except Exception as e: # Catches other errors
  print('\ne')
GPIO.cleanup() # Cleans up GPIO ports