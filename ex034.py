from datetime import date
from colorama import Fore, Style
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
c = Fore.MAGENTA
s = Style.RESET_ALL
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}O ano de {} é Bissexto{}'.format(c, ano, s))
else:
    print('{}O ano de {} não é Bissexto{}'.format(c, ano, s))