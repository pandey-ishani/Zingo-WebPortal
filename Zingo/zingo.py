from firebase import firebase  
from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication
from flask import Flask, redirect, url_for, render_template, request, session, flash
import requests
import json


app = Flask(__name__)


firebase = FirebaseApplication('https://zingo-cc821.firebaseio.com/', authentication = None)  


URL = 'http://www.way2sms.com/api/v1/sendCampaign'



@app.route('/')

def index():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return "Hello!"
 

@app.route('/login', methods=['POST'])
def do_admin_login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		return redirect(url_for('dashboard'))
	else:
		flash('wrong password!')
		return index()


@app.route('/dashboard', methods = ['GET'])
def dashboard():
	return render_template('dashboard.html')


@app.route('/validateGoods', methods = ['GET', 'POST'])
def validate():
	return render_template('tinder.html')

@app.route('/notify', methods = ['GET'])
def notify():
	x={"hello": {'phone': '9013921377', 'message': "The returned goods have been verified at HUL depot. Lifebuoy Liquid Handwash, Bru Instant and Axe Deo. The refund will be generated shortly. For more help, contact 02239830000."}}

	for key, value in x.items():
		print("loop", value['phone'], value['message'])
		sendPostRequest(value['phone'], value['message'])
	return "Refund Process initiated successfully!"

def sendPostRequest(phone, message):
	print("func", phone, message)
	req_params = {
	'apikey': 'QUK8YNYOQFDLPDWHX84YA2MGJAF5GPQI',
	'secret':'XJJO9Q6TSLB8K7HI',
	'usetype': 'stage',
	'phone': phone,
	'message': message
	}
	return requests.post(URL, req_params)

	
if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0')


 


