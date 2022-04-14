import requests
import json

#Токен бота
TOKEN = '5251873233:AAETvAcswfgqoLrN9Yp_Z8ZseriqHYUdO2s'

#Токен API
PAYLOAD = {
    'access_key': 'c0589593f5536f7bd14f6a0e4cb04382'
}

#Валюты по умолчанию
keys = {
    'RUB': 'Russian Ruble',
    'USD': 'United States Dollar',
    "EUR": "Euro"
}

#Считывание списка валют с обменника
#r = requests.get('http://api.exchangeratesapi.io/v1/symbols', params=PAYLOAD)
#keys = json.loads(r.content)['symbols']