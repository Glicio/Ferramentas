import datetime
import re

def formatData(data):
    data = str(data).rsplit()
    data = data[0].rsplit("-")
    return data[2]+"/"+data[1]+"/"+data[0]
def formatNumeroMemorando(data,numero):
    data = re.split("-| ",str(data))
    numero = str(numero)
    if len(numero) == 1:
        numero = "00"+numero
    elif len(numero) == 2:
        numero = "0"+numero
    return f"{data[2]}.{data[1]}.{numero}/{data[0]}"