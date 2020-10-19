from random import randint
from colorama import Fore
from time import sleep
item = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
opcoes = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
if opcoes > 2 or opcoes < 0:
    print('{}JOGADA INVÁLIDA'.format(Fore.RED))
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 11)
    print('Computador jogou {}'.format(item[computador]))
    print('Você jogou {}'.format(item[opcoes]))
    print('-=' * 11)
    if computador == 0: #Se o computador escolher PEDRA
        if opcoes == 0:
            print('EMPATE.')
        elif opcoes == 1:
            print('VOCÊ VENCEU!')
        elif opcoes == 2:
            print('O COMPUTADOR VENCEU!.')
    elif computador == 1: #Se o computador escolher PAPEL
        if opcoes == 0:
            print('O COMPUTADOR VENCEU!')
        elif opcoes == 1:
            print('EMPATE.')
        elif opcoes == 2:
            print('VOCÊ VENCEU!')
    elif computador == 2: #Se o computador escolher TESOURA
        if opcoes == 0:
            print('VOCÊ VENCEU!')
        elif opcoes == 1:
            print('O COMPUTADOR VENCEU.')
        elif opcoes == 2:
            print('EMPATE.')



