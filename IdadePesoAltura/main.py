from Scripts.Cadastro import RecebePessoa,resultados

for i in range(1,16):
    peso = float(input(f"Qual o peso da pessoa {i}?: "))
    altura = float(input(f"Qual a altura da pessoa {i}?: "))
    idade = int(input(f"Qual a idade da pessoa {i}?: "))
    RecebePessoa(altura,peso,idade)

Paltura, Ppeso, Pidade = resultados()
soma = 0

for altura in Paltura:
    soma+=altura

media_altura = soma/len(Paltura)
percent_peso = len(Ppeso)*6.66
idade_50 = len(Pidade)


print(f"""
Temos {idade_50} pessoas acima de 50 anos.
A média de altura das pessoas entre 20 e 30 anos é {media_altura:.2f}.
{percent_peso:.2f}% por cento das pessoas pesam menos de 60 quilos.
""")