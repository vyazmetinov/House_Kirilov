import yaml
from yaml.loader import SafeLoader
with open('token.yml') as f:
    token = yaml.load(f, SafeLoader)['token']

headers = {
    "Content-Type": "application/json",
    "Authorisation": "Bearer {token}".format(token=token)
}