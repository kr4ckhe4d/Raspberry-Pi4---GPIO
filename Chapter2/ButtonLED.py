import RPi.GPIO as GPIO

ledPin = 11
buttonPin = 12
ledStatus = False

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
def loop():
    GPIO.add_event_detect(buttonPin,GPIO.FALLING, bouncetime=300)
    while True:
        if GPIO.event_detected(buttonPin):
            dostuff()
                
def dostuff():
    global ledStatus
    if GPIO.input(buttonPin)==GPIO.LOW:
        if ledStatus==False:
            ledStatus = True
            GPIO.output(ledPin,GPIO.HIGH)
            print('led turned on >>>')
        else:
            ledStatus = False
            GPIO.output(ledPin,GPIO.LOW)
            print('led turned off >>>')
    else :
        if ledStatus==True:
            print('led turned on >>>')
        else:
            print('led turned off >>>')
            
def destroy():
    GPIO.remove_event_detect(buttonPin)
    GPIO.cleanup()
    
if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()