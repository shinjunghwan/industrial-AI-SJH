import RPi.GPIO as GPIO
import time
import spidev

pin = 25
pwm_power = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 50)

def analog_read(channel):
	r = spi.xfer2([1, (0x08+channel)<<4, 0])
	adc_out = ((r[1]&0x03)<<8) + r[2]
	return adc_out
	
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

while True:
    adc = analog_read(1)
    voltage = adc*3.3/1023
    print("adc = %s(%d) voltage = %.3fV" % (hex(adc), adc, voltage))
    pwm_power = 100 - (adc/10)
    if pwm_power > 0:
        pwm.start(pwm_power)
    else:
        pwm.start(0)
    time.sleep(0.5)


pwm.stop()
GPIO.cleanup()

