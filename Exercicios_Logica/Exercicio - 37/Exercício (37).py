"""/*
O cardápio de uma lanchonete é o seguinte:
    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades
# desejadas.

# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total
# geral do pedido.

# Considere que o cliente deve informar quando o pedido deve ser encerrado.
*/"""

#   Especificação   Código  Preço
#     Cachorro Quente 100     R$ 1,20
#     Bauru Simples   101     R$ 1,30
#     Bauru com ovo   102     R$ 1,50
#     Hambúrguer      103     R$ 1,20
#     Cheeseburguer   104     R$ 1,30
#     Refrigerante    105     R$ 1,00


d = {}

try:
    while True:
        codigo = int(input('Código do produto: '))
        qtde = int(input('Quantidade: '))

        if codigo == 0:
            break
        elif codigo < 100 or codigo > 105:
            print('Valores Inválidos')
            break
        else:
            d.update({codigo:qtde})
except ValueError as error:
    print('Valores inválidos inseridos')

preco = preco_2 = preco_3 = preco_4 = preco_5 = preco_6 = 0

t = t2 = t3 = t4 = t5 = t6 = 0
for i in d:
    match i:
        case 100:
            v = d[100]
            preco = v * 1.2
            t += v

        case 101:
            v2 = d[101]
            preco_2 = v2 * 1.3
            t2 += v2

        case 102:
            v3 = d[102]
            preco_3 = v3 * 1.5
            t3 += v3
        
        case 103:
            v4 = d[103]
            preco_4 = v4 * 1.2
            t4 += v4

        case 104:
            v5 = d[104]
            preco_5 = v5 * 1.3
            t5 += v5

        case 105:
            v6 = d[105]
            preco_6 = v6 * 1
            t6 += v6
        case _:
            break


total = preco + preco_2 + preco_3 + preco_4 + preco_5 + preco_6
print(f"Total: R${total:.2f}")