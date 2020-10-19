from colorama import Fore, Style
n = int(input('Digite um número qualquer: '))
c = Fore.YELLOW
s = Style.RESET_ALL
if n % 2 == 0:
    print("o número {}{}{} é par".format(c, n, s))
else:
    print("o número {}{}{} é impar".format(c, n, s))