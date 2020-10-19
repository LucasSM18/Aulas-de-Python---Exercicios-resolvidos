r = float(input("Digite quantos reais você tem na carteira: R$"))
d = r/3.27
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

print("Conversão em dolar: {}US${:.2f}{}".format(cores['cian'], d, cores['limpar']))