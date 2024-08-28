"""/*
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
*/"""

letra = input('insira letra ')[0]
letra = letra.capitalize()

match letra:
    case "A":
        print('Vogal')
    case "E":
        print('Vogal')
    case "I":
        print('Vogal')
    case "O":
        print('Vogal')
    case "U":
        print('Vogal')
    case _:
        print('Não é vogal')