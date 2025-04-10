import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
import json



url1 = "https://my-json-server.typicode.com/M4PANU72/Json-api-webserver/tools"
response1 = requests.get(url1)

url2 = "https://my-json-server.typicode.com/M4PANU72/Json-api-webserver/winkels"
response2 = requests.get(url2)

if response1.status_code != 200:
    print("Fout bij het ophalen van de website")
    exit()

if response2.status_code != 200:
    print("Fout bij het ophalen van de website")
    exit()

print("Website succesvol opgehaald!")
list1 = []
for t in response1.json():
    list1.append({"ID": t["id"], "name": t["name"], "function": t["function"], "category": t["category"]})

list2 = []
for t in response2.json():
    list2.append({"ID": t["id"], "name": t["name"], "address": t["address"]})

print(tabulate(list1, headers="keys", tablefmt="grid"))
print(tabulate(list2, headers="keys", tablefmt="grid"))
