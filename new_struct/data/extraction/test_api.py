import requests
from requests.auth import HTTPBasicAuth
import json
from jsonmerge import merge
result = 0

for id in range(106248, 138569):
	response = requests.get("https://api.ulule.com/v1/projects/%s" %id, auth=HTTPBasicAuth('apikey', 'f8e3a8f4d466c0ba0a0d23ae50651ea84ab96c4b')).json()
	if id%100==0: print(id)
	if len(response)>10:
		#print(result)
		with open('data/data'+str(id)+'.json', 'w', encoding='utf-8') as f:
			json.dump(response, f)




