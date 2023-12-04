import requests
import json
import yaml
from yaml.loader import SafeLoader
import json

import requests
import yaml
from yaml.loader import SafeLoader

with open('token.yml') as f:
    t = yaml.load(f, Loader=SafeLoader)['token']

mess_url = "https://api.avito.ru/realty/v1/"
def get_all_rest():
    url = mess_url + "accounts/{user_id}/items/{item_id}/bookings".format(user_id="31313578", item_id="1992292943")
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {token}".format(token=t)
        }
        params = {
            "date_start": "2023-12-04",
            "date_end": "2023-12-20"
        }
        rent = requests.get(url, headers=headers, params=params)
        print(json.loads(rent.text))
        return json.loads(rent.text)
    except Exception as e:
        print(e)

def main():

    f = open("rents.txt", "w")
    b = False
    for i in get_all_rest():
        # if i == '[':
        #     b = True
        # if(b):
        f.write(i)
if __name__ == "__main__":
    main()


