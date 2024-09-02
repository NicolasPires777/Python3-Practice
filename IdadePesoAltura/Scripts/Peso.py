pesos = []

def RecebePeso(object):
    if object["peso"] < 60:
        pesos.append(object["peso"])