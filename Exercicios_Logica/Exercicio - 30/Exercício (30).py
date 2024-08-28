"""/*
Faça um programa que calcule o valor total investido por um colecionador em sua
coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
*/"""

qcd = int(input('qtde cds '))
vqcd = qcd
l = []


while vqcd != 0:
    vcds = int(input('valor cd '))

    if vcds > 0 :
        add = l.append(vcds)
        media = sum(l) / len(l)
        vqcd -= 1
    else:
        print('Valor inválido')

print(media)