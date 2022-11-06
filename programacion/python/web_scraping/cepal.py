import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        }


url = 'https://api-cepalstat.cepal.org/cepalstat/api/v1/indicator/1/data?members=265%2C29190&lang=es&format=json&in=1'

response = requests.get(url, headers=headers)

data = response.json()


for i in data["body"]["data"]:
    print(i["value"], i["iso3"])




