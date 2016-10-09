import requests
from time import sleep

token = "c37f66112e05713cfd0c0a598d8f6e01a59d2a0a1143580692b5faac34193dff"
# 		ID da minha lampada: 
#		"id": "d073d502164d",
#	 	"uuid": "021063bb-1cae-416b-bbff-3dbe5cc22a35",

headers = {
    "Authorization": "Bearer %s" % token,
}

state_off ={
  "power": "off",
  "color": "blue saturation:0.5",
  "brightness": 0.5,
}

state1 ={
  "power": "on",
  "color": "yellow",
  "brightness": 0.5,
}

state2 ={
  "power": "on",
  "color": "rgb:0,140,251",
  "brightness": 1,
}


# URL base a ser acessada
url_1 = 'https://api.lifx.com/v1/lights/all'
url_2 = 'https://api.lifx.com/v1/scenes'
url_3 = 'https://api.lifx.com/v1/lights/d073d502164d/state'
url_4 = 'https://api.lifx.com/v1/lights/d073d502164d/toggle'

# Request GET - lista todas as lampadas
response = requests.get(url_1,headers=headers)
print(response.text)

#scenes = requests.get(url_2, data={}, headers=headers)
#print(scenes.text)

#t_power = requests.post(url_4,headers=headers)
#print(t_power.text)

activate = requests.put('https://api.lifx.com/v1/lights/d073d502164d/state', data={"power": "on","color": "rgb:128,128,128","brightness": 251}, headers=headers)

#activate = requests.put('https://api.lifx.com/v1/lights/d073d502164d/state', data=state2, headers=headers)
#sleep(5)
#activate = requests.put('https://api.lifx.com/v1/lights/d073d502164d/state', data=state1, headers=headers)
#sleep(5) 
#activate = requests.put('https://api.lifx.com/v1/lights/d073d502164d/state', data=state_off, headers=headers)
#print(activate.text)

'''
cycles=0
while cycles == 0: 	
	sleep(2) 
	t_power = requests.post(url_4,headers=headers)
	print(t_power.text)
'''

