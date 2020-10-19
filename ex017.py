from colorama import Fore, Style
km = float(input("Quantos Km foram percorridos no carro alugado? "))
d = int(input("Por quantos dias ele foi alugado? "))
c = d*60 + km*0.15
co = Fore.LIGHTCYAN_EX
s = Style.RESET_ALL

print("Total a se pagar: {}R${:.2f}{}".format(co, c, s))