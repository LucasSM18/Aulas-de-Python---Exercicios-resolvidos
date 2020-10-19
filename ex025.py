num = int(input("Digite um número entre 0 e 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
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
print("Analisando o número {}{}{}".format(cores['cian'], num, cores['limpar']))
print("Unidade: {}{}{}".format(cores['cian'], u, cores['limpar']))
print("Dezena: {}{}{}".format(cores['cian'], d, cores['limpar']))
print("Centena: {}{}{}".format(cores['cian'], c, cores['limpar']))
print("Milhar: {}{}{}".format(cores['cian'], m, cores['limpar']))