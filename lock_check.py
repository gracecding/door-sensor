import time # so we can use "sleep" to wait between actions
import RPi.GPIO as GPIO # import the GPIO library we just installed but call it "io"
#from ISStreamer.Streamer import Streamer # import the IS Streamer we just installed but call it "Streamer"
#Firebase configuration
import pyrebase
config = {
    "apiKey": "AIzaSyAFepMQwghWlvGVs5eLeUeejTkpwlAT5zM",
    "authDomain": "doorlock-502ed",
    "databaseURL": "https://doorlock-502ed.firebaseio.com",
    "storageBucket": "doorlock-502ed.appspot.com"
}
firebase = pyrebase.initialize_app(config)

#Firebase database initialization
db = firebase.database()

## set GPIO mode to BCM
## this takes GPIO number instead of pin number
GPIO.setmode(GPIO.BCM)
 
## enter the number of whatever GPIO pin you're using
door_pin = 23
 
## use the built-in pull-up resistor
GPIO.setup(door_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # activate input with PullUp
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
 
## initialize door 
door=0
 
## this loop will execute the if statement that is true
while True:
    ## if the switch is open
    if GPIO.input(door_pin):
        #logger.log("Door","Open") # stream a message saying "Open"
        #logger.flush() # send the message immediately
        print("Not Locked")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21, True)
        door=0 # set door to its initial value
        
        data = "Not Locked"
        db.child("lock").set(data)
        
        time.sleep(1) # wait 1 second before the next action
    ## if the switch is closed and door does not equal 1
    if (GPIO.input(door_pin)==False and door!=1):
        #logger.log("Door","Close") # stream a message saying "Close"
        #logger.flush() # send the message immediately
        print("Locked")
        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21, False)
        
        data = "Locked"
        db.child("lock").set(data)
        
        time.sleep(1)
        #door=1 # set door so that this loop won't act again until the switch has been opened