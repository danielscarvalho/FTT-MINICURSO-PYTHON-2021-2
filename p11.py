# pip install requests

import requests

URL="https://api.github.com/users/danielscarvalho/repos"

response = requests.get(URL)
repos = response.json() #dicionario do Python

file = open("gitrepo.tsv","w")

for n in repos:
    print(n["name"], n["id"])
    file.write("{}\t{}\n".format(n["name"], n["id"]))

file.close()