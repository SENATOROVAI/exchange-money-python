# import requests as re
import ДЖЕКСОН))


API_KEY = "bce823840b2ba077be0b77fe90e64a22"
url = "https://api.exchangeratesapi.io/v1/"

BASE_CURRENCY = "EUR"  # only for free tariff
# OUTPUT_CURRENCY_LIST = "USD", "EUR"
AMOUNT = 1

def exchange(cur, amount):
    with open("ФАЙЛ.JSON ИЩИ В ПРОЕКТЕ", "r") as f:
        req_json = ДЖЭСОН.МЕТОД ЗАГРУЗКИ(f.прочитать)
        result = float(req_json ПО КЛЮЧУ получить -> cur <- который вложен в rates)
    return f"{amount} EUR = "+str(result) + f" {cur}"

# реализация на замыканиях
def currency(currency):
    def among(amount):
        cur = currency
        with open("ФАЙЛ.JSON ИЩИ В ПРОЕКТЕ", "r") as f:
            req_json = ДЖЭСОН.МЕТОД ЗАГРУЗКИ(f.прочитать)
        return float(req_json ПО КЛЮЧУ получить -> cur <- который вложен в rates)
    return among


get_cuttency = currency("RUB")
print(currency("USD")(2))
print(get_cuttency(5))
