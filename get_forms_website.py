import requests
from bs4 import BeautifulSoup
page = requests.get('http://localhost:9000/index.html').text
soup = BeautifulSoup(page, 'html.parser')
forms = soup.find_all('form')
for form in forms:
   print(form)

