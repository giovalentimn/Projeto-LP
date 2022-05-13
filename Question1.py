#Nome: Giovanna Valentim Dantas
#RU: 4062459
#Professor: Renan Portela
#Disciplina: Lógica de Programação e Algoritmos
#Atividade Prática - Exercício 01

print("Bem vindo a Loja de Bordados da Giovanna Valentim Dantas")

valor = float(input("Insira o valor do produto: "))
qty = float(input("Insira a quantidade do produto: "))
total = valor * qty
desc = total * (5/100)
desct = total - desc
desc2 = total * (10/100)
desct2 = total - desc2
desc3 = total * (15/100)
desct3 = total - desc3

print("O valor total é R${:.2f}".format(total))

if (qty <= 9):
    print("Esta quantidade não recebe desconto. Portanto, o valor é R${:.2f}".format(total))
elif (qty <= 99):
    print("Esta quantidade recebe um desconto de 5%. Portanto, o valor é R${:.2f}".format(desct))
elif (qty <= 999):
    print("Esta quantidade recebe um desconto de 10%. Portanto, o valor é R${:.2f}".format(desct2))
else:
    print("Esta quantidade recebe um desconto de 15%. Portanto, o valor é R${:.2f}".format(desct3))

print("Volte sempre!")