import requests as re
import json


API_KEY = ""
base_url = "https://api.exchangeratesapi.io/v1/"

status_code = re.get(base_url).status_code

response = f'https://api.exchangeratesapi.io/v1/symbols?access_key = {API_KEY}'

with open("data", "w") as outfile:
    json.dump(response, outfile)
