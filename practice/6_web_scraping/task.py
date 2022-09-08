import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/most-active"

req = requests.get(url)

cont = BeautifulSoup(req.content, "html.parser")
print(cont.prettify())
