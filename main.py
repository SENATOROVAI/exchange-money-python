import requests as re
import json, pprint, os


API_KEY = "3b657357d9c210c7bcee8ce37875e685"
base_url = "https://currate.ru/"

# req_ = re.get(f'https://currate.ru/api/?get=currency_list&key={API_KEY}')

# req_to_json = json.loads(get_currncy_list.text)

if os.path.exists('req.json')==0:    
    with open('req.json', 'w') as outfile:
        json.dump(req_to_json, outfile, ensure_ascii=False, indent=4)



# get =  https://currate.ru/api/?get=rates&pairs=USDRUB,EURRUB&key=YOUR-API-KEY
