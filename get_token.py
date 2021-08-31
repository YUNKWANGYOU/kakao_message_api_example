import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'ea4fb06fe79bda9c16dbb9c4002ddc7b'
redirect_uri = 'https://example.com/oauth'
authorize_code = '3rTO8zGIbMkGRrBZBgYNd5iOtURXGEiG8KV3qT7ZwqlgcddMv-fVUlMNPmO0RnVRg5iF4Qo9dNsAAAF7m314tg'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
with open(r"kakao_code.json","w") as fp:
    json.dump(tokens, fp)

#2.
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)
