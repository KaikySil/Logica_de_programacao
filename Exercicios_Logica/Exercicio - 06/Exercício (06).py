"""/*
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
    equilátero, isósceles ou escaleno.

Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
*/"""

# PEDIR LADOS
l1 = int(input('lado 1 '))
l2 = int(input('lado 2 '))
l3 = int(input('lado 3 '))


# triângulo:
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:

    # equilatero:
    if l1 == l2 and l2 == l3:
        print('equilatero')


    # isoceles:
    if l1 == l2 or l1 == l3 or l2 == l3:
        print('isoceles')
        


    # escaleno:
    if l1 != l2 and l1 != l3 and l2 != l3:
        print('escaleno')