from colorama import Fore, Style
l = float(input("Insira a largura da parede em metros: "))
h = float(input("Insira a altura da parede em metros: "))
a = l*h
qt = a/2
c = Fore.LIGHTMAGENTA_EX
s = Style.RESET_ALL

print(" Área da parede: {}{} m²{}\n Quantidade de tinta necessária: {}{} l{}".format(c, a, s, c, qt, s))