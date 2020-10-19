from colorama import Fore, Style
n = input("Digite o nome de uma cidade: ").strip()
c = Fore.GREEN
s = Style.RESET_ALL
print(c, n[:5].capitalize() == 'Santo', s)