pizzas = []

class Pizza:
    def __init__(self, code, desc, valor_m, valor_g):
        self.code = code
        self.desc = desc
        self.valor_m = valor_m
        self.valor_g = valor_g
        pizzas.append(self)

    
def mostraCardapio():
    for pizza in pizzas:
        print(f"{pizza.code} - Pizza de {pizza.desc}: \n   M - R${pizza.valor_m:.2f}\n   G - R${pizza.valor_g:.2f}\n")

pizza1 = Pizza(21, "Napolitana", 40, 60)
pizza2 = Pizza(22, "Margherita", 35, 55)
pizza3 = Pizza(23, "Calabresa", 45, 65)
pizza4 = Pizza(24, "Portuguesa", 60, 80)
pizza5 = Pizza(25, "Frango", 50, 70)
