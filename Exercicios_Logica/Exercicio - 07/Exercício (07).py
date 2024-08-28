"""/*
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma
é uma data válida.
*/"""

data = input('data (dd/mm/aa) ').split()

data = [int(datas) for datas in data]

if data[0] > 31:
    print('dia invalido ')

elif data[1] > 12:
    print('mês inválido ')
elif data[2] < 0:
    print('ano inválido')
else:
    print('Dia: {} \nMês: {} \nAno: {}' .format(data[0],data[1], data[2])) 
