import requests as re
import json, pprint, os


API_KEY = "3b657357d9c210c7bcee8ce37875e685"
base_url = "https://currate.ru/"

status_code = re.get(base_url).status_code

get_currncy_list = re.get(f'https://currate.ru/api/?get=currency_list&key={API_KEY}')
# g_list = get_currncy_list.text[1:-1:].replace(',', '\n')

req_ = json.loads(get_currncy_list.text)

with open('req.json', 'w') as outfile:
    json.dump(req_, outfile,ensure_ascii=False,indent=4)

# with open ('currensy_list', 'w') as outfile:
#     outfile.write(get_currncy_list)



# with open("currency_list.json", "w") as w_file:
#     json.dump(get_currncy_list['data'], w_file)




# get =  https://currate.ru/api/?get=rates&pairs=USDRUB,EURRUB&key=YOUR-API-KEY




# with open("data.json", "w") as outfile:
#     json.dump(get_currncy_list, outfile)
# print()
