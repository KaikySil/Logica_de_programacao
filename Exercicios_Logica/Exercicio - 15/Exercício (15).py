"""/*
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
*/"""

mora = int(input('Morango '))
maca = int(input('Maçã '))
total_kg = mora + maca

if mora <= 5:
    v_mora = mora * 2.5
elif mora > 5:
    v_mora = mora * 2.2

if maca <= 5:
    v_maca = maca * 1.8
elif mora > 5:
    v_maca = maca * 1.5

total_rs = v_maca + v_mora


if total_kg >= 8 or total_rs >= 25:
    total_des = total_rs * 0.1
    total_des = total_rs - total_des 
    print(f'{mora} kgs de morango \n{maca} kgs de maçã \nTotal kgs: {total_kg}kgs \ntotal rs: {total_des}')
else:
    print(f'{mora} kgs de morango \n{maca} kgs de maçã \nTotal kgs: {total_kg}kgs \ntotal rs: {total_rs}')