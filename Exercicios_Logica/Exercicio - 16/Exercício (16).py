import sys

"""/*
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:

                      Até 5 Kg           Acima de 5 Kg
Filé Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
de carne da promoção, porém não há limites para a quantidade de carne
por cliente.

Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de
5% sobre o total da compra.

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra:
    tipo de carne
    quantidade de carne
    preço total
    tipo de pagamento
    valor do desconto
    valor a pagar.
*/"""

try:
    # pedir nome da carne
    c = input('Digite o nome da carne: \nFilé Duplo - F \nAlcatra - A \nPicanha - P \nDigite: ')
    c = c.capitalize()
    # pedir quantidade de carne
    q = float(input('Digite a quantidade da carne em kgs '))

    print('-' * 30)

    # se a quantidade for menor que 5kg
    if q <= 5:
        # se a carne for Filé Duplo
        if c == 'F':
            tc = 'Filé Duplo'
            # quantidade x 4.9
            total = q * 4.9
        # se for Alcatra
        elif c == 'A':
            tc = 'Alcatra'
            # quantidade x 5.9
            total = q * 5.9
        # se for Picanha
        elif c == 'P':
            tc = 'Picanha'
            # quantidade x 6.9
            total = q * 6.9
        else:
            print('Nome inválido')
            sys.exit()

    # se a quantidade for maior que 5kg
    if q > 5:
        # se a carne for Filé Duplo
        if c == 'F':
            tc = 'Filé Duplo'
            # quantidade x 5.8
            total = q * 5.8
        # se for Alcatra
        elif c == 'A':
            tc = 'Alcatra'
            # quantidade x 6.8
            total = q * 6.8
        # se for Picanha
        elif c == 'P':
            tc = 'Picanha'
            # quantidade x 7.8
            total = q * 7.8
        else:
            print('Nome inválido')
            sys.exit()

    # perguntar se vai pagar no cartão
    cartao = input('Vai pagar no cartão da loja? (s/n) ')
    cartao = cartao.capitalize()

    # se sim
    if cartao == 'S':
        f = 'Cartão da loja'
        # diminui 5% do valor total
        d = total * 0.05
        total -= d
    # senão
    else:
        # pergunta qual a forma de pagamento
        f = input('Qual a forma de pagamento? ')

    print('=' * 30)
    # tipo de carne
    print(f'Carne: {tc}')
    # quantidade de carne
    print(f'Quantidade {q}kgs')
    # tipo de pagamento
    print(f'Tipo de pagamento: {f}')
    # valor do desconto
    if cartao == 'S':
        print('Desconto: 5%')
    else:
        print('Desconto: 0%')
    # valor a pagar.
    print(f'Valor a pagar R${total:.2f}')
    print('=' * 30)

except ValueError as error:
    print('-' * 25)
    print('Valores inválidos')
    print('-' * 25)