from random import randint
from colorama import Fore, Style
computador = randint(0, 5)
s = Style.RESET_ALL
print('-=-' * 10)
print('Pensei em um número entre 0 e 5...')
print('-=-' * 10)
n = int(input('Qual número eu pensei? '))

if n == computador:
    c = Fore.BLUE
    print('\n{}Você acertou, parabens!{}'.format(c, s))
else:
    c = Fore.RED
    print('\n{}Você errou, sinto muito{}'.format(c, s))
    print('número correto: {}'.format(computador))