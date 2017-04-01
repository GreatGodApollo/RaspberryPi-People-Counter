from ubidots import ApiClient # Imports ubidots
import RPi.GPIO as GPIO # Imports GPIO
import time # Imports time for sleep
GPIO.setmode(GPIO.BCM) # Sets GPIO mode
GPIO.setup(7, GPIO.IN) # Sets pin 7 as an input
try:
	api = ApiClient("Your Api Key Here") # Account containing the variable
	poeple = api.get_variable("Your variable here") # Variable for saving to
	print("Connected to Ubidots") # Confirms connection
except: 
	print("Failed to connect to Ubidots, please check your key and internet.") # Gives error if it can't connect to ubidots
counter = 0 # Sets counter level
peoplelev = 0 # Sets people level
while(1):
	presence = GPIO.input(7) # Checks pin for input
	if(presence):
		peoplelev += 1 # Increases people level
		presence = 0 # Resets pin input
		print("Person Passed") # Console output to confirm
		time.sleep(1.5)
		counter += 1
		if(counter==5):
			people.save_value( {'value':peoplelev} ) # Send value to ubidots
      print("Value sent to Ubidots") # Console output to confirm
			counter = 0 # Resets counter
			peoplelev = 0 # Resets people level
