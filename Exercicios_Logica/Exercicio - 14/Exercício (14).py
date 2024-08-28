"""/*
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
*/"""

c = (input('Tipo comprado '))
q = int(input('Quantidade comprada ')) 

c = c.capitalize()

if c == 'G':
    p = q * 2.5

    if q <= 20:
        d = p * 0.03
        total = p - d

    elif q > 20:
        d = p * 0.05
        total = p - d

    print('Litros: {} \nValor {}' .format(q, total))


if c == 'A':
    p = q * 1.9

    if q <= 20:
        d = p * 0.04
        total = p - d

    elif q > 20:
        d = p * 0.6
        total = p - d

    print('Litros: {} \nValor {}' .format(q, total))

else:
    print('Valores inválidos')