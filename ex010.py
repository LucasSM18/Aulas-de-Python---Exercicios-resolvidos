from colorama import Fore, Style
m = float(input("Digite quantos metros você percorreu: "))
km = m*100
mm = m*1000
c = Fore.MAGENTA
s = Style.RESET_ALL

print("{} m = {} cm = {}{}{} mm".format(m, km, c, mm, s))