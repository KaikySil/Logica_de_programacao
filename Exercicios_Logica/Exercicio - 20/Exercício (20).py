"""
/*
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
*/"""

# pedir nome
n = str(input('Insira seu nome: '))
tn = len(n)

while tn < 3:
    print('-' * 25)
    print('Nome inválido')
    print('-' * 25)

    n = str(input('Insira seu nome: '))
    tn = len(n)
    

print('-' * 25)


# pedir idade
i = int(input('Idade: '))

while i <= 0 or i > 110:
    print('-' * 25)
    print('Idade invalida')
    print('-' * 25)
    i = int(input('Idade: '))


print('-' * 25)


# pedir salario
s = int(input('Salario: '))

while s < 0:
    print('-' * 25)
    print('Salário invalido')
    print('-' * 25)
    s = int(input('Salario: '))


print('-' * 25)


# pedir sexo
sx = ''
while sx != 'f' and sx != 'm':
    sx = input('Sexo \nF - Feminino \nM - Masculino \n')
    sx = sx.casefold()
    match sx:
        case 'f':
            hm = 'Feminino'
        case 'm':
            hm = 'Masculino'
        case _:
            print('-' * 25)
            print('Sexo inválido')
            print('-' * 25)

print('-' * 25)
# pedir estado civil - match case
ec = ''
while ec != 's' and ec != 'c' and ec != 'v' and ec != 'd':
    ec = input('Estado civil \nS - Solteiro \nC - Casado \nV - Viúvo \nD - Divorciado \n')
    ec = ec.casefold()
    match ec:
        case 's':
            scvd = 'Solteiro'
        case 'c':
            scvd = 'Casado'
        case 'v':
            scvd = 'Viúvo'
        case 'd':
            scvd = 'Divorciado'
        case _:
            print('-' * 25)
            print('Estado Civil inválido')
            print('-' * 25)

print('=' * 25)

n = n.title()
print(f'Nome: {n} \nIdade: {i} anos \nSalário: R${s} \nSexo: {hm} \nEstado Civil: {scvd}(a)')

print('=' * 25)