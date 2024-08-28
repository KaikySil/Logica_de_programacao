"""/*
Faça um programa que peça para n pessoas a sua idade, ao final o programa
deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e
maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
média calculada.
*/"""



l = []
r = 's'
try:
    while r == 's':
        n1 = float(input('n1 '))
        print('-' * 20)
        r = input('Reiniciar? (s/n): ')

        l.append(n1)
        soma = sum(l)
        media = soma / len(l)
        
        if r != 's':
            print('-' * 20)
            print(f'Média: {media}')
        
        

    if media >= 0 and media <= 25:
        print('jovem')
    elif media > 25 and media < 60:
        print('adulto')
    else:
        print('idoso')
except ValueError as error:
    print('errado')