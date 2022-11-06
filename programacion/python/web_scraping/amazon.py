import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    "authority": "loadus.exelator.com"
        }

libros_totales = []

url_api = 'https://loadus.exelator.com/load/?p=204&g=8888&j=0' 

response = requests.get(url_api, headers=headers)

print(response)

"""
data = response.json()

libros = data["courses"]


for libro in libros:
    libros_totales.append(
            {
                "title": libro["title"],
                "num_reviews": libro["num_reviews"],
                "rating": libro["rating"],
            }
        )

df = pd.DataFrame(libros_totales)

print(df)

df.to_csv('libros_amazon.csv')
"""
