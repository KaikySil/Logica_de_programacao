"""/*
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar.

O resultado da operação deve ser acompanhado de uma
frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
*/"""


n1 = int(input('valor1: '))
n2 = int(input('valor2: '))

op = input('operador, + - x ou /: ')



if op == '+' or op == 'soma':
    r = n1 + n2
    pi = r % 2
    de = r % 1


elif op == '-' or op == 'menos':
    r = n1 - n2
    pi = r % 2
    de = r % 1


elif op == 'x' or op == 'vezes':
    r = n1 * n2
    pi = r % 2
    de = r % 1


elif op == '/' or op == 'divisao':
    r = n1 / n2
    pi = r % 2
    de = r % 1

print(r)
if pi == 0:
    print('Par')
if r <0:
    print('negativo')
else:
    print('positivo')
if de == 0:
    print('inteiro')
else:
    print('decimal')
