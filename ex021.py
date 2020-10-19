from random import choice
from colorama import Fore, Style
a1 = input("Digite o nome do 1° aluno: ")
a2 = input("Digite o nome do 2° aluno: ")
a3 = input("Digite o nome do 3° aluno: ")
a4 = input("Digite o nome do 4° aluno: ")
c = Fore.LIGHTGREEN_EX
s = Style.RESET_ALL

lista = [a1, a2, a3, a4]

print("O aluno que apagará o quadro será o {}{}{}".format(c, choice(lista), s))