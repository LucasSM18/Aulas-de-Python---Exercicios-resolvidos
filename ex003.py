n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
s = int(n1) + int(n2)
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
print("{} + {} = {}{}".format(n1, n2, cores['yellow'], s))