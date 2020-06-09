import requests
import json

url = "https://openapi.naver.com/v1/search/movie"
client_id = "ejOUQkCYzvQKxcQB9C7U"
client_secret = "QNkvPM3696"
query_string = "?query=뭐지&display=100"
header = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-secret": client_secret
}

r = requests.get(url + query_string, headers=header)
print(r.text)
print(r.url)
print(json.loads(r.text))