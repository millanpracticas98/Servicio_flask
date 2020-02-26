from flask import Flask, render_template, request, redirect, url_for
from contador import *
import json

app = Flask(__name__)

modelos = {None: contador()}


@app.route("/")
def index():
    return modelos.get(None).num_palabras("dfasdlhfkja asfhuasfh aslfhs lkjshlfjksahlsfahjkh js ljjkafh")

@app.route("/contador/<string:idioma>/<string:texto>")
@app.route("/contador/<string:texto>", methods=['GET', 'POST'], defaults={'idioma': None})
def consulta(idioma, texto):
    #print(request.args.get('c'))
    caracter = request.args.get('c')
    modelo = modelos.get(caracter)
    if modelo == None:
        modelo = contador(caracter)
        modelos.update({caracter : modelo})
    return modelo.num_palabras(texto,idioma)

@app.route("/contador", methods=['GET', 'POST'])
def consulta2():
    data = request.get_json()
    modelo = modelos.get(data["caracter"])
    if modelo == None:
        modelo = contador(data["caracter"])
        modelos.update({data["caracter"] : modelo})
    return modelo.num_palabras(data["texto"],data["idioma"])




if __name__ == '__main__':
    app.run(threaded=True)