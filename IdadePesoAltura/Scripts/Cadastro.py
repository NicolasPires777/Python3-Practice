from .Altura import RecebeAltura, alturas
from .Peso import RecebePeso, pesos
from .Idade import RecebeIdade, idades

pessoas = []
def RecebePessoa(altura, peso, idade):
    pessoa = {
        "altura":altura,
        "peso": peso,
        "idade":idade
    }
    pessoas.append(pessoa)


def resultados():
    for pessoa in pessoas:
        RecebeAltura(pessoa)
        RecebeIdade(pessoa)
        RecebePeso(pessoa)
    return alturas, pesos, idades
