from flask import Flask, abort, request 
from flask import render_template
import time
import _thread
from goprocam import GoProCamera
from goprocam import constants
import base64
import re
import requests
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient()
db = client.gopro
collection = db.order_ids

print("Establishing Connection with the Camera")
gopro = GoProCamera.GoPro(constants.gpcontrol)
	
		
		
def stream():
	print("Starting the live stream")
	gopro.stream("udp://127.0.0.1:1000", "high")
	print("Stopping the live stream")


@app.route('/')
def hello():
	return "Hello World"
	
@app.route('/images')
def show_images():
	items = collection.find({})
	return render_template('index.html', items=items)

@app.route('/screenshot', methods=['POST'])
def take_screenshot():
	order_id = request.values['orderid']
	gpcam = GoProCamera.GoPro(constants.gpcontrol)
	image_url = gpcam.take_photo()
	save_to_database(order_id, image_url)
	return ''

def save_to_database(order_id, image_url):
	post = {"order_id": order_id, "image_url": image_url}
	collection.insert_one(post).inserted_id

if __name__ == '__main__':
	print("Starting the Web Server")
	_thread.start_new_thread( stream, () )
	app.run()
	print("Stopped")