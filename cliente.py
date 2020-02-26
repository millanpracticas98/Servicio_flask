import requests
import json

url = "http://127.0.0.1:5000/contador"
data = {'caracter': 'i', 'idioma': 'fr', 'texto': 'We did it!'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)


print(r.text)



"""pip install requests"""