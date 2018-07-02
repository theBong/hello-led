from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name="Treehouse"):
	return "Hello from "+ name


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
	return "{}".format(num1 + num2)

app.run(debug=True, port=800, host='0.0.0.0')
