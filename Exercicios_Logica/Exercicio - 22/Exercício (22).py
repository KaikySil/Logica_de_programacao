"""/*
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
*/"""
for i in range (1, 51):
    impar = i % 2
    if impar != 0:
        print(i)