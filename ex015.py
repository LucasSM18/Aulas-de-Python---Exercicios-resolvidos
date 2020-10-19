from colorama import Fore, Style
s = float(input("Digite o seu valor salárial: R$"))
a = s + (s * 15/100)
c = Fore.LIGHTBLUE_EX
sty = Style.RESET_ALL

print(" Salário incial: {}R${:.2f}{}\n".format(c, s, sty),
      "Salário com aumento de 15%: {}R${:.2f}{}".format(c, a, sty))
