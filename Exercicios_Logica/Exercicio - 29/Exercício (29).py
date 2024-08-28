"""/*
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de
alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
*/"""



# lista vazia
l = []
# pedir quantidade de turmas
t = int(input('Insira quantas turmas há na escola '))
n = 1

# enquanto variavel "t" for diferente de 0
while t != 0:
    # pedir quantidade de alunos
    a = int(input(f'Digite a quantidade de alunos da turma {n}: '))
    

    # turma nao pode ter mais que 40 alunos
    if a > 0 and a <= 40:
        # adicionar a quantidade de alunos na lista
        add = l.append(a)
        # diminuir um no valor de turmas
        t -= 1
        n += 1

    # caso coloque 0, número negativo ou mais que 40
    else:
        print('quantidade invalida!')

# calcular a média somando todos os itens da lista e dividindo pelo tamanho da lista
m = (sum(l)) / len(l)
print(f'A média de alunos é de: {m:.1f}')