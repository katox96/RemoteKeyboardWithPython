from flask import Flask, send_from_directory
from pynput.keyboard import Key, Controller

app = Flask(__name__)
keyboard = Controller()

@app.route("/")
def index():
	return send_from_directory('./', 'key.html')

@app.route('/key/<key>')
def hello_world(key):
	keyboard.press(key)
	keyboard.release(key)
	return key

if __name__ == '__main__':
   app.run(host= '0.0.0.0')