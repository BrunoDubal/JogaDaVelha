from random import randint
from re import T
from turtle import clear

print('Jogo da Velha')

layout = [[' ', ' ', ' '],
[' ', ' ', ' '],
[' ', ' ', ' ']]


def verifica_empate():
    resultado = True
    for l in layout:
        for c in l:
            if ' ' in c:
                resultado = False
    return resultado
                

def tabela():
    for lin in layout:
        for col in lin:
            print(f'|{col}', end ='')
        print('|')

tabela()
    
cont_jogador = 1

bot = int(input('''Gostaria de jogar contra um Bot? 
[1]SIM
[2]NÃO
'''))

while True:

    if layout[0][0] + layout[0][1] + layout[0][2] == 'XXX' or layout[0][0] + layout[1][0] + layout[2][0] == 'XXX':
        print('Jogador Xis ganhou')
        break
    elif layout[1][0] + layout[1][1] + layout[1][2] == 'XXX' or layout[0][1] + layout[1][1] + layout[2][1] == 'XXX':
        print('Jogador Xis ganhou')
        break
    elif layout[2][0] + layout[2][1] + layout[2][2] == 'XXX' or layout[0][2] + layout[1][2] + layout[2][2] == 'XXX':
        print('Jogador Xis ganhou')
        break
    elif layout[0][0] + layout[1][1] + layout[2][2] == 'XXX' or layout[0][2] + layout[1][1] + layout[2][0] == 'XXX':
        print('Jogador Xis ganhou')
        break


    if layout[0][0] + layout[0][1] + layout[0][2] == 'OOO' or layout[0][0] + layout[1][0] + layout[2][0] == 'OOO':
        print('Jogador Circulo ganhou')
        break
    elif layout[1][0] + layout[1][1] + layout[1][2] == 'OOO' or layout[0][1] + layout[1][1] + layout[2][1] == 'OOO':
        print('Jogador Circulo ganhou')
        break
    elif layout[2][0] + layout[2][1] + layout[2][2] == 'OOO' or layout[0][2] + layout[1][2] + layout[2][2] == 'OOO':
        print('Jogador Circulo ganhou')
        break
    elif layout[0][0] + layout[1][1] + layout[2][2] == 'OOO' or layout[0][2] + layout[1][1] + layout[2][0] == 'OOO':
        print('Jogador Circulo ganhou')
        break


    if verifica_empate():
        print('Deu velha')
        break


    if bot == 1:
        if cont_jogador == 1:
            jogador = 'X'
            try:
                while True:
                    print(f'Faça sua jogada com {jogador} ')
                    l = int(input('Digite a linha: '))
                    c = int(input('Digite a coluna: '))
                    if ' ' in layout[l-1][c-1]:
                        layout[l-1][c-1] = jogador
                        tabela()
                        print('\n\n\n')
                        cont_jogador = 2
                        break
                    else:
                        print('Campo ja contem uma jogada. Tente outro campo.')
            except:
                print('Opção invalida. Por favor tente novamente')


        elif cont_jogador == 2:
            jogador = 'O'
            try:
                while True:
                    l = int(randint(0,2))
                    c = int(randint(0,2))
                    if ' ' in layout[l][c]:
                        layout[l][c] = jogador
                        tabela()
                        print('\n')
                        cont_jogador = 1
                        break
            except:
                print('Opção invalida. Por favor tente novamente.')
    
    
    else:
        if cont_jogador == 1:
            jogador = 'X'
            try:
                while True:
                    print(f'Faça sua jogada com {jogador} ')
                    l = int(input('Digite a linha: '))
                    c = int(input('Digite a coluna: '))
                    if ' ' in layout[l-1][c-1]:
                        layout[l-1][c-1] = jogador
                        tabela()
                        cont_jogador = 2
                        break
                    else:
                        print('Campo ja contem uma jogada. Tente outro campo.')
            except:
                print('Opção invalida. Por favor tente novamente')


        elif cont_jogador == 2:
            jogador = 'O'
            try:
                while True:
                    print(f'Faça sua jogada com {jogador} ')
                    l = int(input('Digite a linha: '))
                    c = int(input('Digite a coluna: '))
                    if ' ' in layout[l-1][c-1]:
                        layout[l-1][c-1] = jogador
                        tabela()
                        cont_jogador = 1
                        break
                    else:
                        print('Campo ja contem uma jogada. Tente outro campo.')
            except:
                print('Opção invalida. Por favor tente novamente.')