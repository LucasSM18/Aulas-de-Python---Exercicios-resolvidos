n = float(input("Digite um número: "))
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
print("número: {}{}{}\nPorção inteira: {}{}{}".format(cores['cian'], n, cores['limpar'], cores['cian'], int(n), cores['limpar']))