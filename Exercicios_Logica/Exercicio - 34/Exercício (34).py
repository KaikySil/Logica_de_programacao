"""/*
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.
*/"""


l = []

temperatura = 1
while temperatura != 0:
    temperatura = int(input('temp '))
    l.append(temperatura)

l.remove(0)

print(f"Maior: {max(l)} \nMenor: {min(l)} \nMédia: {(sum(l)) / len(l):.2f}")