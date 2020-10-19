from colorama import Fore, Style
s = float(input('Qual é o salário do funcionário? R$'))
c = Fore.BLUE
c2 = Fore.RED
sty = Style.RESET_ALL
if s > 1250:
    a = s + (s * 0.1)
else:
    a = s + (s * 0.15)
print('Quem ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}{}'.format(c2, s, sty, c, a, sty))