from cardapio.cardapio import pizzas

carrinho = []

def adiciona_pizza(code, tamanho):
    for pizza in pizzas:
        if code == pizza.code:
            sabor = pizza.desc
            if tamanho.upper() == 'M':
                preco = pizza.valor_m
                break
            elif tamanho.upper() == 'G':
                preco = pizza.valor_g
                break
    carrinho.append({"code": code, "sabor": sabor, "tamanho": tamanho, "preco":preco})
    return "Pizza adicionada ao carrinho"

def mostra_Carrinho():
    carrinho_str = ""
    i = 1
    for item in carrinho:
        carrinho_str += f"Item {i}: Pizza de {item['sabor']} tamanho {item['tamanho']}. R${item['preco']:.2f}\n"
        i += 1
    return carrinho_str

def calculo_total():
    total = 0
    for item in carrinho:
        total += item["preco"]
    return total

def num_pizza():
    return len(carrinho)

def entrega(valor):
    if valor == True:
        adicional = 10
        deliver = "Entrega"
    else:
        adicional = 0
        deliver = "Balcão"
    return adicional, deliver

def finaliza(ent):
    numero_pizzas = num_pizza()
    add_entrega, resposta = entrega(ent)
    total_carrinho = calculo_total()
    total = total_carrinho+add_entrega
    print(f"""Pedido enviado: \n
Você pediu {numero_pizzas} pizzas.
São elas:\n{mostra_Carrinho()}
Para retirar: {resposta}
Valor: R${total:.2f}
""")