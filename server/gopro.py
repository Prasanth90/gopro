from flask import Flask, abort, request 
import time
import _thread
from goprocam import GoProCamera
from goprocam import constants
import base64
import re


app = Flask(__name__)
print("Establishing Connection with the Camera")
gopro = GoProCamera.GoPro(constants.gpcontrol)
	
		
def stream():
	print("Starting the live stream")
	gopro.livestream("start")
	gopro.stream("udp://127.0.0.1:1000", "high")
	print("Stopping the live stream")


@app.route('/')
def hello():
	return "Hello World"

@app.route('/screenshot', methods=['POST'])
def get_image():
    image_b64 = request.values['imageBase64']
    order_id = request.values['orderid']
    print(image_b64)
    print(order_id)
    k = base64.b64encode(image_b64.encode())
    with open("imageToSave.jpg", "wb") as fh:
    	fh.write(base64.decodebytes(k))
    return ''

if __name__ == '__main__':
	print("Starting the Web Server")
	_thread.start_new_thread( stream, () )
	app.run()
	print("Stopped")