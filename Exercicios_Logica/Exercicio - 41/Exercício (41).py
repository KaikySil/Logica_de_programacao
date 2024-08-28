"""
Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as
temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
d = {
    "Janeiro": 0,
    "Fevereiro": 0,
    "Março": 0,
    "Abril": 0,
    "Maio": 0,
    "Junho": 0,
    "Julho": 0,
    "Agosto": 0,
    "Setembro": 0,
    "Outubro": 0,
    "Novembro": 0,
    "Dezembro": 0,
}



for i in d:
    temperatura = int(input(f'Insira a temperatura de {i}: '))
    d.update({i:temperatura})
    l = d.values()
    media = sum(l) / len(l)

print('Meses maiores que a média:')

if d["Janeiro"] > media:
    print(f'Janeiro - {d["Janeiro"]}°C')

if d["Fevereiro"] > media:
    print(f'Fevereiro - {d["Fevereiro"]}°C')

if d["Março"] > media:
    print(f'Março - {d["Março"]}°C')

if d["Abril"] > media:
    print(f'Abril - {d["Abril"]}°C')

if d["Maio"] > media:
    print(f'Maio - {d["Maio"]}°C')

if d["Junho"] > media:
    print(f'Junho - {d["Junho"]}°C')

if d["Julho"] > media:
    print(f'Julho - {d["Julho"]}°C')

if d["Agosto"] > media:
    print(f'Agosto - {d["Agosto"]}°C')

if d["Setembro"] > media:
    print(f'Setembro - {d["Setembro"]}°C')

if d["Outubro"] > media:
    print(f'Outubro - {d["Outubro"]}°C')

if d["Novembro"] > media:
    print(f'Novembro - {d["Novembro"]}°C')

if d["Dezembro"] > media:
    print(f'Dezembro - {d["Dezembro"]}°C')


print(f'Média total: {media:.0f}°C') 