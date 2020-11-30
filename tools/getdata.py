from config.configuration import db, collection

def person_sentence(nombre):
    """
    Una query a la base de datos para obtener las frases de un personaje de Juego de Tronos
    """
    query = {"Name":f"{nombre}"}
    frases = list(collection.find(query,{"_id":0, "Release Date":0}))
    return frases

