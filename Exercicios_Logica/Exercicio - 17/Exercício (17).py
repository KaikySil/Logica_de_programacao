"""/*
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
usuário informe um valor válido.
*/"""

nota = 11
while nota > 10 or nota < 0:

# pedir nota entre 0 - 10
    nota = int(input('nota '))
    if nota > 10 or nota < 0:
        # mostrar erro se for invalido
        print('Valor inválido')
# repetir ate ser válido