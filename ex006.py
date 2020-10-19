from colorama import Fore, Style
c = Fore.BLUE
s = Style.RESET_ALL

x = input("Digite qualquer caracter ou uma cadeia de caracteres: ")
print('''Esse valor é da classe: {}{}{} \nÉ alfabético? {}{}{} \nÉ numérico? {}{}{} 
É alfanumérico? {}{}{} \nTem espaço? {}{}{} \nÉ maiusculo? {}{}{} 
É minusculo? {}{}{} \nÉ capitalizada? {}{}{}'''
      .format(c, type(x), s, c, x.isalpha(), s, c, x.isnumeric(),
              s, c, x.isalnum(), s, c, x.isspace(),
              s, c, x.isupper(), s, c, x.islower(), s, c, x.istitle(), s))
