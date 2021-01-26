import requests
import json
import sys

the_data = dict()

### return 0 if problem, else return the json payload
url = "https://rand.tennisbowling.com/random"
load = requests.get (url).json()
if load['status'] != 'OK':
    print("api is working as intended")
else:
    sys.exit("Api did not return 200 ok. please check api.")


