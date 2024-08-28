"""/*
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
*/"""


# pedir tamanho arquivo
arquivo = int(input('Insira o tamanho do arquivo (em MB) '))
# pedir velocidade de link em Mbps
velo = int(input('Insira a velocidade da internet '))

mbps = velo / 8

tempo = arquivo / mbps
print('Demorará {:.0f} minutos para completar o download' .format(tempo))