from flask import Flask, render_template, request, redirect, url_for
from contador import *

app = Flask(__name__)

modelo = contador()


@app.route("/")
def index():
    return modelo.num_palabras("dfasdlhfkja asfhuasfh aslfhs lkjshlfjksahlsfahjkh js ljjkafh")

@app.route("/contador/<string:idioma>/<string:texto>")
@app.route("/contador/<string:texto>", methods=['GET', 'POST'], defaults={'idioma': None})
def consulta(idioma, texto):
    print(idioma)
    print(texto)
    print(request.args.get('c'))
    return modelo.num_palabras(texto,idioma)



if __name__ == '__main__':
    app.run(threaded=True)