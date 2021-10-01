# Dicionário ou dict = JSON

# pip install requests

# virtual env

import requests



def call_ddg(query):
    URL="https://api.duckduckgo.com/?format=json&pretty=1&q=" + query
    resp = requests.get(URL)
    data = resp.json()
    return data["Abstract"] #Chave do dicionário...

while True:
    txt = input("Query text: ")
    if len(txt) == 0:
        break
    print(call_ddg(txt))
    print("\n")
