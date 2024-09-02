faixa1 = []
faixa2 = []
faixa3 = []
faixa4 = []
faixa5 = []

for i in range(1,16):
    while True:
        idade = int(input(f"Qual a idade da pessoa {i}: "))
        if idade < 0:
            print("Erro! A idade não pode ser menor que Zero")
        elif 0<= idade <=15:
            faixa1.append(idade)
            print("Usuário Adicionado! \n")
            break
        elif 16<= idade <=30:
            faixa2.append(idade)
            print("Usuário Adicionado! \n")
            break
        elif 31<= idade <=45:
            faixa3.append(idade)
            print("Usuário Adicionado! \n")
            break
        elif 46<= idade <=60:
            faixa4.append(idade)
            print("Usuário Adicionado! \n")
            break
        elif 61<= idade:
            faixa5.append(idade)
            print("Usuário Adicionado! \n")
            break

percent_faixa1 = len(faixa1)*6.66
percent_faixa2 = len(faixa2)*6.66
percent_faixa3 = len(faixa3)*6.66
percent_faixa4 = len(faixa4)*6.66
percent_faixa5 = len(faixa5)*6.66

print("="*40)
print(" "*11,"RELATÓRIO DE IDADES"," "*10)
print("="*40)

print(f"""
Tivemos {len(faixa1)} pessoas cadastradas com idade até 15 anos, isso representa {percent_faixa1:.2f}% do total.
Tivemos {len(faixa2)} pessoas cadastradas com idade entre 16 e 30 anos, isso representa {percent_faixa2:.2f}% do total.
Tivemos {len(faixa3)} pessoas cadastradas com idade entre 31 e 45 anos, isso representa {percent_faixa3:.2f}% do total.
Tivemos {len(faixa4)} pessoas cadastradas com idade entre 46 e 60 anos, isso representa {percent_faixa4:.2f}% do total.
Tivemos {len(faixa5)} pessoas cadastradas com idade acima de 61 anos, isso representa {percent_faixa5:.2f}% do total.
""")