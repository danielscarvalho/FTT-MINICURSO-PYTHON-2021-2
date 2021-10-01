# Dicionário ou dict = JSON

# pip install requests

# virtual env

import requests

URL="https://api.duckduckgo.com/?format=json&pretty=1&q=Sonia+Braga"

resp = requests.get(URL)
print(resp)

data = resp.json();
print(type(data))

print(data["Abstract"])