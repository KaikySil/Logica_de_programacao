"""/*
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.
*/"""

l1 = 0
while l1 < 21:
    print(l1)
    l1 += 1


l2 = [0]
while len(l2) < 20:
    for i in l2:
        add = l2.append(1 + i)
        
        if len(l2) > 20:
            break
print(l2)