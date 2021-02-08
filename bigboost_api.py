from requests import request

url = "https://bigboost.bigdatacorp.com.br/peoplev2?Datasets=basic_data&q=doc{xxxxxxxxxxx}&AccessToken="
payload = {}
headers = {
  'Content-Type': 'application/json'
}
response = request("GET", url, headers=headers, data = payload)
print(response.text.encode('utf8'))

