from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
pin =26
state = 0

GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, state)

@app.route('/')
@app.route('/toggle')
def toggle():
	state += 1
	state %= 2
	GPIO.output(pin, state)
	return "state = {}".format(str(state))



app.run(debug=True, port=800, host='0.0.0.0')
