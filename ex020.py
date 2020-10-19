from math import sin, cos, tan, radians
a = float(input("Digite um ângulo qualquer: "))
r = radians(a)
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
print("Ângulo: {}{}{}\nSeno: {}{:.2f}{}".format(cores['gray'], a, cores['limpar'], cores['gray'], sin(r), cores['limpar']),
      "\nCosseno: {}{:.2f}{}\nTangente: {}{:.2f}{}".format(cores['gray'], cos(r), cores['limpar'], cores['gray'], tan(r), cores['limpar']))