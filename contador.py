import json

class contador(object):
    def __init__(self, caracter = None):
        self.caracter = caracter
    def num_palabras(self, texto="", idioma = "es"):
        if idioma== None:
            idioma = "es"
        if self.caracter:
            dev = {
                "NumOcurrencias": texto.count(self.caracter),
                "caracter": self.caracter,
                "idioma": idioma,
                "texto": texto
            }
            return json.dumps(dev)
        else:
            np = 0
            for aux in texto.split(" "):
                np =np + 1
            dev = {
                    "npalabras": np,
                    "idioma": idioma,
                    "texto": texto
                }
            return json.dumps(dev)