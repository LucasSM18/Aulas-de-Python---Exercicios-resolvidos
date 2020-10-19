from colorama import Fore, Style
nome = input("Digite o seu nome completo: ").strip()
u = nome.upper()
l = nome.lower()
c = len(nome) - nome.count(" ")
s = nome.split()
col = Fore.LIGHTYELLOW_EX
sty = Style.RESET_ALL


print("""\nSeu nome em maiusculo: {}{}{}
Seu nome em minusculo: {}{}{}
Quantidade de caracteres no nome: {}{}{}
Primeiro nome é {}{}{} e a quantidade de caracters é {}{}{}"""
      .format(col, u, sty, col, l, sty, col, c, sty, col, s[0], sty, col, nome.find(' '), sty))