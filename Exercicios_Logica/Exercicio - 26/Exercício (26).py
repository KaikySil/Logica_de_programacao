"""
/*
Faça um programa que calcule o mostre a média aritmética de N notas.
*/
"""

l = []
r = 's'

while r == 's':
    n1 = float(input('n1 '))
    print('-' * 20)
    r = input('Reiniciar? (s/n): ')

    l.append(n1)
    soma = sum(l)
    media = soma / len(l)
    
    if r != 's':
        print('-' * 20)
        print(f'Média: {media}')