import requests
import json
import jsonpath

url = "http://localhost:3000/api/collection/"
header = {'Content-Type': 'application/json', 'X-Metabase-Session': '82f2696e-58f8-477a-8ef3-c6c762c91746'}


def testPostCollection():
    f = open('collection_data.json', 'r')
    # json_input = f.read()
    json_request = json.loads(f.read())
    response = requests.post(url, json=json_request, headers=header)

    assert response.status_code == 200