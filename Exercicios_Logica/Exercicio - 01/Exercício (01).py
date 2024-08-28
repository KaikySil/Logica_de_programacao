"""# /*
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
# o rendimento diário de seu trabalho.

# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
# regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
# de R$ 4,00 por quilo excedente.

# João precisa que você faça um programa que leia a variável peso
# (peso de peixes) e calcule o excesso.

# Gravar na variável excesso a quantidade de quilos além do limite"""

resp = 's'
while resp == 's':
    peso_max = 50
    peso = int(input('Insira o peso do peixe '))

    valor = peso - peso_max

    if valor >= 1:
        multa = valor * 4 
        print("Excedeu o limite por {}kgs, terá que pagar a multa no valor de R${} " .format(valor, multa))
    else:
        print("Não excedeu o limite, não terá que pagar a multa")

    resp = input("Reiniciar? (s/n) ")