from colorama import Fore, Style
frase = input("Digite uma frase: ").upper().strip()
c = Fore.CYAN
s = Style.RESET_ALL
print("A letra 'A' aparece {}{} vezes{}".format(c, frase.count('A'), s))
print("Ela aparece pela primeira vez na posição {}{}{}".format(c, frase.find('A') + 1, s))
print("Ela aparece pela ultima vez na posição {}{}{}".format(c, frase.rfind('A') + 1, s))