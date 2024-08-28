"""/* 85
Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código.
Os códigos utilizados são:
    1, 2, 3, 4  - Votos para os respectivos candidatos
    (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco

Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos.

Para finalizar o conjunto de votos tem-se o valor zero.
*/"""

# mostrar opções
print('1 - J \n2 - K \n3 - L \n4 - M \n5 - Nulo \n6 - Branco')

j = k = l = m = nulo = branco = 0

while True:
    voto = input('Voto: ')

    match voto:
        case '1':
            j += 1

        case '2':
            k += 1
        
        case '3':
            l += 1

        case '4':
            m += 1

        case '5':
            nulo += 1

        case '6':
            branco += 1

        case _:
            break

votos_totais = j + k + l + m
porc_nulos = (nulo / votos_totais) * 100
porc_branco = (branco / votos_totais) * 100

print(f'Votos candidato J: {j} \nVotos candidato K: {k} \nVotos candidato L: {l} \nVotos candidato M: {m}')
print(f'Votos Nulos: {nulo} \nVotos Brancos: {branco}')
print(f'A percentagem de votos nulos sobre o total de votos é de: {porc_nulos:.2f}%')
print(f'A percentagem de votos em branco sobre o total de votos é de {porc_branco:.2f}%')