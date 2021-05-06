import datetime

def formatData(data):
    data = str(data).rsplit()
    data = data[0].rsplit("-")
    return data[2]+"/"+data[1]+"/"+data[0]