import requests
payload = {'uname': 'tjalle', 'pass': 'tjalle'}
r = requests.post('http://localhost:9000/cuser.php', data=payload)
print(r.status_code)
