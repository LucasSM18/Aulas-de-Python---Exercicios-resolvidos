v = float(input("Digite o preço de um produto: R$"))
d = v - (v * 5/100)
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

print(" Preço do produto: {}R${:.2f}{}\n".format(cores['purple'], v, cores['limpar']),
      "Com desconto de 5%: {}R${:.2f}{}".format(cores['purple'], d, cores['limpar']))

