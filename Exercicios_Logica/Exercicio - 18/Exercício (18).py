"""/*
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.
*/"""

n = ''
s = ''

while n == s:
    # inserir nome
    n = input('Nome: ')
    n = n.casefold()

    # inserir senha
    s = input('Senha: ')
    s = s.casefold()

    # se nome e senha forem iguais
    if n == s:
        print('O nome e a senha não podem ser iguais, por favor digite novamente')
    # senão
    else:
        print('Cadastrado')