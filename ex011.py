from colorama import Fore, Style
n = int(input("Digite um número: "))
i = 0
c = Fore.YELLOW
s = Style.RESET_ALL
while i <= 10:
    print("{} x {} = {}{}{}".format(n, i, c, n*i, s))
    i += 1