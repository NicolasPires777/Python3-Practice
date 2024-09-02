def descIR (salario):
    if salario<=2259.20:
        desconto = 0
    elif salario >= 2259.21 and salario <= 2826.65:
        desconto = salario * 0.075
    elif salario >= 2826.66 and salario <= 3751.05:
        desconto = salario * 0.15
    elif salario >= 3751.06 and salario <= 4664.68:
        desconto = salario * 0.225
    elif salario > 4664.69:
        desconto = salario * 0.275
    else:
        Exception("Ocorreu um erro ao calcular o desconto do Imposto de Renda")
    return desconto