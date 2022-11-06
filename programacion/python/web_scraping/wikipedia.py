# Request
import requests
# parciar
from lxml import html
# dataframe
import pandas as pd

# Datos de navegador, para que la página no reconozca que estamos haciendo web scraping
encabezados = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    }

# Request
url = "https://es.wikipedia.org/wiki/Diego_Maradona"

# Requerimiento
respuesta = requests.get(url,headers=encabezados)

# imprimir parciador
parser = html.fromstring(respuesta.text)

# Podemos obtener el texto anterior de la siguiente manera
años = parser.xpath('//*[@id="mw-content-text"]/div[1]/table[11]/tbody/tr/td/a/text()')
partidos = parser.xpath('//*[@id="mw-content-text"]/div[1]/table[11]/tbody/tr/td/b/text()')

partido,gol,asistencia = [], [], []

for i in range(len(partidos)):
    if i % 4 == 0:
        partido.append(partidos[i])
    elif i % 4 == 1:
        gol.append(partidos[i])
    elif i % 4 == 2:
        asistencia.append(partidos[i])

año = []
for i in range(len(años)):
    año.append(años[i])

# dataframe
df = pd.DataFrame({'año': año, 'partidos': partido, 'goles': gol, 'asistencias': asistencia})
# eliminar las primeras 3 filas y reiniciar index
df = df.iloc[3:].reset_index(drop=True)

# exportar a csv en carpeta data.
df.to_csv('data/maradona.csv', index=False)
