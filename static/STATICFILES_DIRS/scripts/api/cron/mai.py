import json
from datetime import date

import requests

req_token = requests.request("POST", "https://api.avito.ru/token/?grant_type=client_credentials&client_id=i1RWsfzle6jUgZsvrSlh&client_secret=VacQYfLcTpshj_pgE6Kn3sinH5Qw2abmD0Velxva")
data = json.loads(req_token.text)
print(data)
t = data["access_token"]
print(t)

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
        print(date_rents)
        print(json.loads(rent.text))
        return date_rents
    except Exception as e:
        print(e)


def main():
    get_all_rest()
if __name__ == "__main__":
    main()


