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


def exchange(cur, amount):
    with open("exchangerates_req.json", "r") as f:
        req_json = json.loads(f.read())
        result = float(req_json["rates"][cur])
    return f"{amount} EUR = "+str(result) + f" {cur}"

# реализация на замыканиях
def currency(currency):
    def among(amount):
        nonlocal currency
        cur = currency
        with open("exchange-money-python/exchangerates_req.json", "r") as f:
            req_json = json.loads(f.read())
        return float(req_json["rates"][cur])
    return among


get_cuttency = currency("RUB")
print(currency("USD")(2))
print(get_cuttency(5))
