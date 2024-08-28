"""/*
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.
*/"""

c0 = 0
c1 = 0
c2 = 0
c3 = 0

p = int(input('Número de Eleitores: '))
e = p

while e != 0:
    v = input('voto c0, c1, c2, c3: ')
    match v:
        case 'c1':
            c1 += 1
            e -= 1
        case 'c2':
            c2 += 1
            e -= 1
        case 'c3':
            c3 += 1
            e -= 1
        case 'c0':
            c0 += 1
            e -= 1
        case _:
            print('Voto inválido!')
    

print(f'Candidato 1: {c1} votos \nCandidato 2: {c2} votos \nCandidato 3: {c3} votos \nVotos Nulo: {c0}')
