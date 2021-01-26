import requests
import os

response = requests.get(f"https://rand.tennisbowling.com/random")
print(response)
if response == "<Response [200}>":
    exit(0)
else:
    sys.exit("Api response is not 200! Please check the api.")