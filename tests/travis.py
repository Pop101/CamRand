import requests
import json
import sys

the_data = dict()

url = "https://rand.tennisbowling.com/random"
load = requests.get (url).json()
if load['status'] == 'OK':
    print("Api is working as intended.")
else:
    sys.exit("Api is down or not working. please check it.")


