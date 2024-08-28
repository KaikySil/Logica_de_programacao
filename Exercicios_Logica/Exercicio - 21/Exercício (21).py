"""/*
Faça um programa que leia 5 números e informe o maior número.
*/"""
n1 = int(input('numero1 '))
n2 = int(input('numero2 '))
n3 = int(input('numero3 '))
n4 = int(input('numero4 '))
n5 = int(input('numero5 '))

l = []
add = n1, n2, n3, n4, n5
l.extend(add)
m = max(l)
print(m)