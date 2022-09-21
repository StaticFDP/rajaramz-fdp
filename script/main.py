import requests
import os
import json

FDP_INDEX_URL = os.environ['FDP_INDEX_URL']
FDP_URL = os.environ['FDP_URL']

print("Pinging FDP INDEX " + FDP_INDEX_URL + " to index FDP " + FDP_URL)

payload = json.dumps({'clientUrl': FDP_URL})
headers = {'content-type': "application/json"}
response = requests.request("POST", FDP_INDEX_URL, data=payload, headers=headers)
print(response.text)
