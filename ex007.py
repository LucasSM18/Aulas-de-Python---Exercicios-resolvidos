from colorama import Fore, Style

n = int(input("Digite um número: "))
an = n-1
sc = n+1
c = Fore.GREEN
s = Style.RESET_ALL

print(" Valor: {}{}{}\n".format(c, n, s),
      "Antecessor: {}{}{}\n".format(c, an, s),
      "Sucessor: {}{}{}".format(c, sc, s))