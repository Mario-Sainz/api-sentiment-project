from config.configuration import db, collection

def insert_mensaje(temporada, episodio, titulo_episodio, personaje, frase):
    """
    Esta es la función que va a insertar los datos en Mongo
    """
    dict_insert = {"Season" : f"{temporada}",
    "Episode" : f"{episodio}",
    "Episode Title" : f"{titulo_episodio}",
    "Name" : f"{personaje}",
    "Sentence" : f"{frase}"
    }
    collection.insert_one(dict_insert)