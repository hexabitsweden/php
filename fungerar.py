import requests
payload = {'uname': 'kalle', 'pass': 'kalle'}
r = requests.post('http://localhost:9000/cuser.php', data=payload)
print(r.status_code)
