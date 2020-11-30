# api-sentiment-project


# Creación de una API básica de Juego de Tronos, utilizando Flask.
La api tiene un método POST para introducir datos y un método GET para extraer datos

# ¿Cómo funcionan éstos métodos?

# @POST
Endpoint
- /nuevafrase/

Para insertar datos, hay que rellenar:
1- Temporada
2- Episodio
3- Título del episodio
4- Nombre del personaje
5- Frase que dice el personaje


# @GET
Endpoint
- /frases/<nombre>

# ¿Cómo extraer las frases de todos los personajes por temporada o episodio?

Extraemos todas las frases que tenemos de un usuario en la base de datos

```
url_frases = "http://localhost:5000/frases/"
person = "tyrion lannister"
```

# Sentiment Analysis

Por último, se puede apreciar un notebook, llamado "Sentiment analysis", en el cual se pueden realizar análisis de las frases de los personajes en cuanto su tono y sentimientos.
