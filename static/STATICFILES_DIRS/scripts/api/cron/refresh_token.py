import json
import requests
import yaml

req_token = requests.request("POST", "https://api.avito.ru/token/?grant_type=client_credentials&client_id=i1RWsfzle6jUgZsvrSlh&client_secret=VacQYfLcTpshj_pgE6Kn3sinH5Qw2abmD0Velxva")
data = json.loads(req_token.text)
to_yaml = {"token": data["access_token"]}
print(data)
with open("token.yml", "w") as f:
    yaml.dump(to_yaml, f)