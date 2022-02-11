from distutils.command.clean import clean
from random import randint
from turtle import clear

print('Jogo da Velha')

layout = [[' ', ' ', ' '],
[' ', ' ', ' '],
[' ', ' ', ' ']]

def tabela():
    for lin in layout:
        for col in lin:
            print(f'|{col}', end ='')
        print('|')

tabela()
    
    
while True:
    print()
    jogador = str(input('Escolha um jogador: \n[X] ou [O] --> ')).strip().upper()
    if jogador == 'X' or jogador == 'O':
        break
    else:
        print('Opção invalida! Tente digitar X ou O.')


cont_jogador = 0
if jogador == 'X':
    cont_jogador = 1
else:
    cont_jogador = 2


while True:
    print()
    if cont_jogador == 1:
        jogador = 'X'
        while True:
            print(f'Faça sua jogada com {jogador} ')
            l = int(input('Digite a linha: '))
            c = int(input('Digite a coluna: '))
            if ' ' in layout[l-1][c-1]:
                layout[l-1][c-1] = jogador
                tabela()
                cont_jogador += 1
                break
            else:
                print('Campo ja contem uma jogada. Tente outro campo.')
    else:
        jogador = 'O'
        while True:
            print(f'Faça sua jogada com {jogador} ')
            l = int(input('Digite a linha: '))
            c = int(input('Digite a coluna: '))
            if ' ' in layout[l-1][c-1]:
                layout[l-1][c-1] = jogador
                tabela()
                cont_jogador -= 1
                break