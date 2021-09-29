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

# Threaded Callback setup
GPIO.setup(i1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(i2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED 1 PWM object 
pwm1 = GPIO.PWM(p1,100)
# LED 2 PWM object 
pwm2 = GPIO.PWM(p2,100)


# LED 1 Threaded Callback function:
def myCallback(i1):
    pwm1.start(0) # Start PWM cycle at 0% duty cycle
    for dc in range(0,100,1): # Iterate PWM from 0 to 100 in increments of 1
      pwm1.ChangeDutyCycle(dc)
      sleep(0.005)
    for dc in range(100,-1,-1):
      pwm1.ChangeDutyCycle(dc)
      sleep(0.005)

# LED 2 threaded callback function:
def myCallback2(i2):
    pwm2.start(0)
    for dc in range(0,100,1):
      pwm2.ChangeDutyCycle(dc)
      sleep(0.005)
    for dc in range(100,-1,-1):
      pwm2.ChangeDutyCycle(dc)
      sleep(0.005)

# Execute LED 1 blink function if port 1 goes HIGH
GPIO.add_event_detect(i1, GPIO.RISING, callback= myCallback, bouncetime=100)
# Execute LED 2 blink function if port 2 goes HIGH
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