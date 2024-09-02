import scripts.carrinho as CR
import cardapio.cardapio as CA
from scripts.controller import recebePedido

print(f"\n\n======== Bem Vindo a Pizzaria do Nico! ========\nAqui está nosso cardápio:\n")
CA.mostraCardapio()

while True:
    sair = False
    pizza = int(input("Qual sabor de pizza você gostaria? Digite apenas o código: "))
    tamanho = input("Qual tamanho da pizza? (M ou G): ")
    resp = recebePedido(pizza, tamanho)
    print(resp,"\n")

    while True:
        decisao = input("Deseja fazer mais algum pedido? [S ou N]: ")
        if decisao.upper() == 'N':
            sair= True
            break
        elif decisao.upper() == 'S':
            break
        else:
            print("Digite 'S' para sim e 'N' para não")

    if sair == True:
        break

print(f"\nSeu carrinho:\n")
carro = CR.mostra_Carrinho()
print(carro)

while True:
        decisao = int(input("\nEscolha uma das opções:\n  1 - Entrega (R$10,00)\n  2 - Buscar na Pizzaria\nDecisão: "))
        if decisao == 1:
            entrega = True
            break
        elif decisao == 2:
            entrega = False
            break
        else:
            print("Digite '1' para entrega ou '2' para buscar")

CR.finaliza(entrega)




