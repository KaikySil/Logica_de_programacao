"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"""


a = float(input('Insira sua altura: '))

p = (72.7 * a) - 58

print(f'Sua altura ideal seria: {p:.0f}kg')