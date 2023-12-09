import json
from datetime import date

import requests
import yaml
from yaml.loader import SafeLoader

with open('static/STATICFILES_DIRS/scripts/api/cron/token.yml') as f:
    t = yaml.load(f, Loader=SafeLoader)['token']

mess_url = "https://api.avito.ru/realty/v1/"

def get_all_rest():
    date_rents = ""
    url = mess_url + "accounts/{user_id}/items/{item_id}/bookings".format(user_id="31313578", item_id="1992292943")
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {token}".format(token=t)
        }
        params = {
            "date_start": "{today}".format(today=date.today()),
            "date_end": "2030-12-30",
            "with_unpaid": "true"
        }
        rent = requests.get(url, headers=headers, params=params)
        d = rent.json()
        for i in range(len(d['bookings'])):
            a = (d['bookings'][i]['check_in'])

            b = d['bookings'][i]['check_out']

            date_rents += str(a) + " "
            date_rents += str(b) + " "

        print(json.loads(rent.text))
        return date_rents
    except Exception as e:
        print(e)

def main():
    get_all_rest()
if __name__ == "__main__":
    main()


