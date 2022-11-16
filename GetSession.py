import requests
import json
import jsonpath

# #Get session
url_session = "http://localhost:3000/api/session"
data = {'username': 'aliahmadazhar4420@gmail.com', 'password': 'Googlo0324!'}
header = {'Content-Type': 'application/json'}
res = requests.post(url_session, data=json.dumps(data), headers=header)
result = res.json()
print(result)
print(res)

#{'id': '82f2696e-58f8-477a-8ef3-c6c762c91746'}