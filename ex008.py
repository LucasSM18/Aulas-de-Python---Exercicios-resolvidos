from colorama import Fore, Style
n = int(input("Insira um número: "))
d = n*2
t = n*3
r = n**(1/2) #exponenciação de 1/2 é a mesma coisa que raiz quadrada
c = Fore.CYAN
s = Style.RESET_ALL

print(" Número: {}{}{}\n Dobro: {}{}{}\n".format(c, n, s, c, d, s),
      "Triplo: {}{}{}\n Raiz Quadrada: {}{}{}".format(c, t, s, c, r, s))