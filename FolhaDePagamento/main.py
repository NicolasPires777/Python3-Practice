from Scripts.CalculoIR import descIR 
from Scripts.CalculoSindicato import descSindicato

bruto = float(input("Quanto vale sua hora de trabalho?: R$"))
horas = float(input("Quantas horas você trabalhou no ultimo mês?: "))
print("")

totalBruto = bruto * horas

desc_IR = descIR(totalBruto)
desc_Sindicato = descSindicato(totalBruto)

liquido = totalBruto-desc_IR-desc_Sindicato

print("="*40)
print(" "*11,"FOLHA DE PAGAMENTO"," "*11)
print("="*40)

print(f"""
Salario Bruto: R${totalBruto:.2f}
Desconto do Sindicato: R${desc_Sindicato:.2f}
Desconto do imposto de renda: R${desc_IR:.2f}
Salário líquido: R${liquido:.2f}
""")