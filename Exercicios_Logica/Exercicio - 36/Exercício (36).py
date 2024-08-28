"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e
valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:
    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25

Exemplo de saída do programa:
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67
"""



# receber valor
valor_divida = int(input('Valor divida: '))

# mostrar tabela
print("""Os juros e a quantidade de parcelas seguem a tabela abaixo: 
Quantidade de Parcelas:  / %  de juros sobre o valor inicial da dívida:
     1                                         0
     3                                        10
     6                                        15
     9                                        20
    12                                        25
""")

# perguntar quantidade de parcelas
qtde_parcelas = int(input('Insira a quantidade de parcelas: '))

# ifs e elses
match qtde_parcelas:
    case 1:
        porc_juros = 0
        valor_juros = 0
    case 3:
        porc_juros = 10
        valor_juros = valor_divida * 0.1
    case 6:
        porc_juros = 15
        valor_juros = valor_divida * 0.15
    case 9:
        porc_juros = 20
        valor_juros = valor_divida * 0.2
    case 12:
        porc_juros = 25
        valor_juros = valor_divida * 0.25
    case _:
        print('inv ')
      
valor_parcela = valor_divida / qtde_parcelas

print('\n')

print(f"Valor da Dívida: R${valor_divida:.2f} \nValor dos Juros: R${valor_juros:.2f} \nQuantidade de Parcelas: {qtde_parcelas} \nValor da Parcela: R${valor_parcela:.2f}")

print('\n')