#pip install requests

import requests

headers = {
    'User-Agent':''
}

response = requests.get('http://127.0.0.1:8000/',headers=headers)
print(response.text)