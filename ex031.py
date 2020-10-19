v = float(input('Qual a velocidade do seu carro atual? '))
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
if v > 80:
    m = (v - 80) * 7
    print('Você ultrapassou o limite de velocidade.')
    print('Você terá que pagar uma multa de {}R${:.2f}{}'.format(cores['gray'], m, cores['limpar']))
print('Tenha um ótimo dia e dirija com cuidado.')