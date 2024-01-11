import requests
payload = {'uname': 'user', 'password': '1234'}
r = requests.post('http://localhost:9000/cuser.php', data=payload)
print(r.status_code)
