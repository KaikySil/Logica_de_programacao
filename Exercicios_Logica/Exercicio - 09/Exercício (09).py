"""/*
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
*/"""

valor = 0
while valor == 0:
    try:
        valor = int(input("Insira valor "))

        match valor:
            case 1:
                print('Domingo')
            case 2:
                print('Segunda')
            case 3:
                print('Terça')
            case 4:
                print('Quarta')
            case 5:
                print('Quinta')
            case 6:
                print('Sexta')
            case _:
                print('Valor inválido')
    except ValueError as error:
        print('letra')