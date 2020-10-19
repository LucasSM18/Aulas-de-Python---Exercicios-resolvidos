from math import hypot
from colorama import Fore, Style

o = float(input("Digite o cateto oposto: "))
a = float(input("Digite o catato adjacente: "))
h = hypot(o, a)
c = Fore.LIGHTRED_EX
s = Style.RESET_ALL

print("{}² + {}² = {}{:.2f}{}".format(o, a, c, h, s))
