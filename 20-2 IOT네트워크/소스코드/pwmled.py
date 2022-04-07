import RPi.GPIO as GPIO
import time

pin = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 50)

pwm.start(50)
time.sleep(10)

pwm.start(60)
time.sleep(10)

pwm.start(100)
time.sleep(10)

pwm.stop()
GPIO.cleanup()
