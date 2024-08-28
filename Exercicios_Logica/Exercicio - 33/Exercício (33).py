"""O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
agora possui uma loja de conveniências.

Faça um programa que implemente uma caixa registradora rudimentar.

O programa deverá receber um número desconhecido de valores referentes aos
preços das mercadorias.

Um valor zero deve ser informado pelo operador para indicar o final da compra.

O programa deve então mostrar o total da compra e perguntar o valor em dinheiro
que o cliente forneceu, para então calcular e mostrar o valor do troco.

Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a
próxima compra.

A saída deve ser conforme o exemplo abaixo:
    Lojas Tabajara
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 8.00
    Dinheiro: R$ 20.00
    Troco: R$ 12.00"""

l = []
while True:
   

    produto = 1
    indice = 0
    while produto != 0:
        produto = float(input('Produto: '))
        l.append(produto)
    total = sum(l)

    print(f'Total: {total:.2f}')
    print('')

    pgto = float(input('Pagamento: '))

    if pgto < total:
        print('Falta dinheiro')
        break
    else:
        troco = pgto - total
        print('Lojas Tabajara:')
        for i in l:
            indice += 1
            print(f'Produto {indice}: R${i:.2f}')
        print(f'Total: R${total:.2f} \nDinheiro: R${pgto} \nTroco: R${troco:.2f}')
        print('-' * 40)