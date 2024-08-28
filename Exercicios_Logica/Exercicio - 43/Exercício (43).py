"""Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C= (5 (F-32)/9)."""


faren = int(input('Insira a temperatura em Farenheit: '))

celsius = (faren - 32) * 5 / 9

print(f'Temeperatura em Celsius: {celsius:.1f}C°')