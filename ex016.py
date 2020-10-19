c = float(input("Informe a temperatura em C°: "))
f = (c * 9/5) + 32
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
print(" Graus em Celsius: {}{}°C{}\n".format(cores['green'],c, cores['limpar']),
      "Graus em Fahrenheit: {}{}°F{}".format(cores['green'], f, cores['limpar']))