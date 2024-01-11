import requests
from bs4 import BeautifulSoup
page = requests.get('http://10.19.95.15/hp/device/set_config_password.html?tab=System&menu=Passwd').text
soup = BeautifulSoup(page, 'html.parser')
forms = soup.find_all('form')
for form in forms:
   print(form)

