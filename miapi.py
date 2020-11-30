from flask import Flask, request
import markdown.extensions.fenced_code
import tools.getdata as get
import json
import tools.postdata as pos





app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string



@app.route("/frases/<nombre>")
def frases_personajes(nombre):
    frases = get.person_sentence(nombre)
    return json.dumps(frases)



@app.route("/nuevafrase/",methods=["POST"])
def insert_mensaje():
    temporada = request.form.get("Season")
    episodio = request.form.get("Episode")
    titulo_episodio = request.form.get("Episode Title")
    personaje = request.form.get("Name")
    frase = request.form.get("Sentence")
    pos.insert_mensaje(temporada, episodio, titulo_episodio, personaje, frase)
    return "Mensaje introducido correctamente a la base de datos"







app.run(debug=True)