"""/*
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares.
*/"""

l = []
l = l
while len(l) < 10:
    n = int(input('Valor: '))
    l.append(n)


par = 0
impar = 0
for i in l:
    imp = i % 2
    if imp != 0:
        par += 1
    else:
        impar += 1
print('-' * 20)
print(f'Há {par} números pares e \n{impar} números ímpares')