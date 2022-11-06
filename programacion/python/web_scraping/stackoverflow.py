import requests
from bs4 import BeautifulSoup

encabezados = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    }

url = 'https://stackoverflow.com/questions'

respuesta = requests.get(url, headers=encabezados)

# parciamos con BeautifulSoup
soup = BeautifulSoup(respuesta.text, 'html.parser')

contenedor_preguntas = soup.find(id="questions")

lista_preguntas = contenedor_preguntas.find_all('div',class_="s-post-summary--content")

for pregunta in lista_preguntas:
    elemento_texto_pregunta = pregunta.find('h3')
    texto_pregunta = elemento_texto_pregunta.text
    descripcion_pregunta = elemento_texto_pregunta.find_next_sibling('div').text
    descripcion_pregunta = descripcion_pregunta.replace('\n','').replace('\r','').strip()
    print(texto_pregunta)
    print(descripcion_pregunta)

