import requests
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random

headers = {'user-agent': user}

link = 'https://browser-info.ru/'
response = requests.get(link, headers = headers).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id = "tool_padding")

# проверка JS
check_js = block.find('div', id = "javascript_check")
status_js = check_js.find_all('span')[1].text
result_js = f'javascript: {status_js}'

print(result_js)

# проверка Flash
check_fl = block.find('div', id = "flash_version")
status_fl = check_fl.find_all('span')[1].text
result_fl = f'flash: {status_fl}'

print(result_fl)

# проверка Cookies
check_cook = block.find('div', id = "cookie_check")
status_cook = check_cook.find_all('span')[1].text
result_cook = f'cookies: {status_cook}'

print(result_cook)

# проверка user_agent
result_user = block.find('div', id = "user_agent").text

print(result_user)













