import pandas as pd
import json
from datetime import datetime
import numpy as np
import advertools as adv
import nltk
from nltk.corpus import stopwords
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import stylecloud
import matplotlib.pyplot as plt

f = open('../data/paginaSiete.json')
data = json.load(f)

title = []

for i in range(len(data)):
    for r in data[i]["titulo"]:
        title.append(r)

df = pd.DataFrame(title, columns=['title'])
df.to_csv('title.csv', index=False)

my_long_list = ["2019", "2017","y","que","con","en","que no","en el","por","para","fue","e","a", "a su","de su","un","a un","no hay","tras","se","sera","hasta","su","son","no","es","de lo","sobre","de la","sus","contra la","de","ante la","el","lo","una","al","ante","le","pero","pide","dice","como","hay","sin","los","está","año","desde","contra la","si","tres","la","dos","años","afirma","más","otro","las","tiene","entre","día","del","ser","medio","va","ir","frente","sea","cuando","da","favor","qué","algún","alguna","algunas","alguno","algunos","ambos","ampleamos","ante","antes","aquel","aquellas","aquellos","aqui","arriba","atras","bajo","bastante","bien","cada","cierta","ciertas","cierto","ciertos","como","con","conseguimos","conseguir","consigo","consigue","consiguen","consigues","cual","cuando","dentro","desde","donde","dos","el","ellas","ellos","empleais","emplean","emplear","empleas","empleo","en","encima","entonces","entre","era","eramos","eran","eras","eres","es","esta","estaba","estado","estais","estamos","estan","estoy","fin","fue","fueron","fui","fuimos","gueno","ha","hace","haceis","hacemos","hacen","hacer","haces","hago","incluso","intenta","intentais","intentamos","intentan","intentar","intentas","intento","ir","la","largo","las","lo","los","mientras","mio","modo","muchos","muy","nos","nosotros","otro","para","pero","podeis","podemos","poder","podria","podriais","podriamos","podrian","podrias","por","por qué","porque","primero","puede","pueden","puedo","quien","sabe","sabeis","sabemos","saben","saber","sabes","ser","si","siendo","sin","sobre","sois","solamente","solo","somos","soy","su","sus","también","teneis","tenemos","tener","tengo","tiempo","tiene","tienen","todo","trabaja","trabajais","trabajamos","trabajan","trabajar","trabajas","trabajo","tras","tuyo","ultimo","un","una","unas","uno","unos","usa","usais","usamos","usan","usar","usas","uso","va","vais","valor","vamos","van","vaya","verdad","verdadera","verdadero","vosotras","vosotros","voy","yo","él","ésta","éstas","éste","éstos","última","últimas","último","últimos","a","añadió","aún","actualmente","adelante","además","afirmó","agregó","ahí","ahora","al","algo","alrededor","anterior","apenas","aproximadamente","aquí","así","aseguró","aunque","ayer","buen","buena","buenas","bueno","buenos","cómo","casi","cerca","cinco","comentó","conocer","consideró","considera","contra","cosas","creo","cuales","cualquier","cuanto","cuatro","cuenta","da","dado","dan","dar","de","debe","deben","debido","decir","dejó","del","demás","después","dice","dicen","dicho","dieron","diferente","diferentes","dijeron","dijo","dio","durante","e","ejemplo","ella","ello","embargo","encuentra","esa","esas","ese","eso","esos","está","están","estaban","estar","estará","estas","este","esto","estos","estuvo","ex","existe","existen","explicó","expresó","fuera","gran","grandes","había","habían","haber","habrá","hacerlo","hacia","haciendo","han","hasta","hay","haya","he","hecho","hemos","hicieron","hizo","hoy","hubo","igual","indicó","informó","junto","lado","le","les","llegó","lleva","llevar","luego","lugar","más","manera","manifestó","mayor","me","mediante","mejor","mencionó","menos","mi","misma","mismas","mismo","mismos","momento","mucha","muchas","mucho","nada","nadie","ni","ningún","ninguna","ningunas","ninguno","ningunos","no","nosotras","nuestra","nuestras","nuestro","nuestros","nueva","nuevas","nuevo","nuevos","nunca","o","ocho","otra","otras","otros","parece","parte","partir","pasada","pasado","pesar","poca","pocas","poco","pocos","podrá","podrán","podría","podrían","poner","posible","próximo","próximos","primer","primera","primeros","principalmente","propia","propias","propio","propios","pudo","pueda","pues","qué","que","quedó","queremos","quién","quienes","quiere","realizó","realizado","realizar","respecto","sí","sólo","se","señaló","sea","sean","según","segunda","segundo","seis","será","serán","sería","sido","siempre","siete","sigue","siguiente","sino","sola","solas","solos","son","tal","tampoco","tan","tanto","tenía","tendrá","tendrán","tenga","tenido","tercera","toda","todas","todavía","todos","total","trata","través","tres","tuvo","usted","varias","varios","veces","ver","vez","y","ya","cij","anuncian","habla","casa","días","exige","pidió","tema","ven","entrega","pedido","grupo","evitar","tema","hechos","paz","ven","hora","deja","busca","mano","presentan","página","califica","obra","llama","papa","recibe","cree","advierte","cargo","asegura","persona","piden","hijo","niega","plantea","horas","video","recurso","declara","son","medida","medios","unidad","anuncia","punto","falta","encuesta"]


stylecloud.gen_stylecloud(file_path="title.csv",
                        size=1024,
                        custom_stopwords=my_long_list,
                        icon_name='fas fa-comment',
                        palette='colorbrewer.diverging.Spectral_7',
                        background_color='#F9F6F0',gradient='vertical',
                        stopwords=adv.stopwords["spanish"]
                        )
