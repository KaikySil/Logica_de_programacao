"""/*
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.

Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
*/"""

print('-' * 25)
valor_hora = int(input('Valor da hora '))
horas_tra = int(input('Horas trabalhadas '))
print('-' * 25)

bruto = horas_tra * valor_hora

inss = bruto * 0.1
fgts = bruto * 0.11


if bruto > 900:
    if bruto > 900 and bruto <= 1500:
        ir = bruto * 0.05

    if bruto > 1500 and bruto <= 2500:
        ir = bruto * 0.10

    if bruto > 2500:
        ir = bruto * 0.2

    total_desc = inss + ir
    liquido = bruto - total_desc
    print("Salário bruto: {:.2f} \n(-) IR: {:.2f} \n(-) INSS: {:.2f} \nFGTS: {:.2f} \nTotal de descontos: {:.2f} \nSalário Líquido: {:.2f}" .format(bruto, ir, inss, fgts, total_desc, liquido))

else:
    total_desc = fgts
    liquido = bruto - total_desc
    print("Salário bruto: {:.2f} \n(-) INSS: {:.2f} \nFGTS: {:.2f} \nTotal de descontos: {:.2f} \nSalário Líquido: {:.2f}" .format(bruto, inss, fgts, total_desc, liquido ))
print('-' * 25)