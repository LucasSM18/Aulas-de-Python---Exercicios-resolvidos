nome = str(input("Digite seu nome completo: ")).strip()
cores = {'limpar': '\033[m',
         'white': '\033[30m',
         'red': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m',
         'blue': '\033[34m',
         'purple': '\033[35m',
         'cian': '\033[36m',
         'gray': '\033[37m'
}
print("Seu nome tem Silva? {}{}{}".format(cores['green'], 'silva' in nome.lower(), cores['limpar']))
