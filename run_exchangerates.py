# import requests as re
import json


API_KEY = "bce823840b2ba077be0b77fe90e64a22"
url = "https://api.exchangeratesapi.io/v1/"

BASE_CURRENCY = "EUR"  # only for free tariff
# OUTPUT_CURRENCY_LIST = "USD", "EUR"
AMOUNT = 1

# req =  re.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base={BASE_CURRENCY}&{OUTPUT_CURRENCY_LIST}").text

# req = re.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY})&base={BASE_CURRENCY}").text

# req = re.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}").text
# req_json = json.loads(req)

# with open("/home/user/git/exchange-money-python/r.json","w")as outfile:
#     json.dump(req_json,outfile,ensure_ascii=False,indent=4)


def exchange(val, amount):
    with open("exchangerates_req.json", "r") as f:
        req_json = json.loads(f.read())
        result = float(req_json["rates"][val])
    return f"{amount} EUR = "+str(result) + f" {val}"

