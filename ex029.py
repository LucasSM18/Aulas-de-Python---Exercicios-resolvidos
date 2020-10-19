nome = input("Digite o seu nome completo: ").strip().split()
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
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}{}{}".format(cores['cian'], nome[0], cores['limpar']))
print("Seu ultimo nome é {}{}{}".format(cores['cian'], nome[-1], cores['limpar'],))