import requests
from bs4 import BeautifulSoup

site = 'http://localhost:9000/index.html'
session = requests.Session()
resp = session.get(site)
html = resp.text

soup = BeautifulSoup(html, 'html')

data = {}
form = soup.find('text', {'uname': 'Password'})
for field in form.find_all('input'):
    try:
        data[field['Password']] = field['value']
    except:
        pass

data['Password'] = 'DanskModer0'
data['ConfirmPassword'] = 'DanskModer0'

post_resp = session.post('http://10.19.78.15/hp/device/set_config_password.html', data = data)


post_soup = BeautifulSoup(post_resp.content , 'html')
#if post_soup.find_all (id='a-page'):
#    print('Login Successfull')
#else:
#    print('Login Failed')

print(post_soup.content)

#<input type="password" class="medium" name="Password" id="Password" accesskey="p" autocomplete="off" maxlength="16" value="*************">

#<input type="password" class="medium" name="ConfirmPassword" id="ConfirmPassword" accesskey="w" autocomplete="off" maxlength="16" value="*************">

 #  Username: <input type="text" name="uname"><br>
 #  Password: <input type="password" name="pass"><br>
