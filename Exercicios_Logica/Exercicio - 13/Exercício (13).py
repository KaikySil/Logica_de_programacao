"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente"."""


print('-' * 25)

print('Telefonou para a vítima?')
r1 = input('s/n ')[0]

print('-' * 25)

print('Esteve no local do crime?')
r2 = input('s/n ')[0]

print('-' * 25)

print('Mora perto da vítima?')
r3 = input('s/n ')[0]

print('-' * 25)

print('Devia para a vítima?')
r4 = input('s/n ')[0]

print('-' * 25)

print('Já trabalhou com a vítima?')
r5 = input('s/n ')[0]

print('-' * 25)

resp = [r1, r2, r3, r4, r5]

t = 0
for i in resp:
    if i == 's':
        t += 1

match t:
    case 1:
        print('Inocente')
    case 2:
        print('Suspeita')
    case 3 | 4:
        print('Cumplíce')
    case 5:
        print('Assassino')