n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
s = n1 + n2
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