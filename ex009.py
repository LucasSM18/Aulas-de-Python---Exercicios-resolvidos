from colorama import Fore, Style
n1 = float(input("Digite a NP1: "))
n2 = float(input("Digite a NP2: "))
ma = (n1+n2)/2
s = Style.RESET_ALL

if ma < 7:
    c = Fore.RED
else:
    c = Fore.BLUE

print("A média aritimética é: {}{}{}".format(c, ma, s))