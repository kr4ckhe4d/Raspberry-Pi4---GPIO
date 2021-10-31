import RPi.GPIO as GPIO
import time

ledPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin,GPIO.OUT)
    GPIO.output(ledPin,GPIO.LOW)
    print('Setup done.')

if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        while True:
            GPIO.output(ledPin,GPIO.HIGH)    
            time.sleep(1)
            GPIO.output(ledPin,GPIO.LOW)
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.output(ledPin,GPIO.LOW)
        GPIO.cleanup()