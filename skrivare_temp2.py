import requests
from bs4 import BeautifulSoup as soup
soup.original_encoding = 'utf-8'

payload = {'uname': 'fredde', 'pass': 'fredde'}
r = requests.post('http://localhost:9000/cuser.php', data=payload)
print(r.status_code)
