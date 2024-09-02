from cardapio.cardapio import pizzas
import scripts.carrinho as CR

def recebePedido(sabor, tamanho):
    for pizza in pizzas:
        if pizza.code == sabor:
            if tamanho.upper() == 'M' or tamanho.upper() == 'G':
                add = CR.adiciona_pizza(sabor, tamanho)
                return add
    return "Código ou Tamanho incorretos, nada foi adicionado ao carrinho"
                