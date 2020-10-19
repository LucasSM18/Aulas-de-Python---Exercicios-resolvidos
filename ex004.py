n = input("Digite qualquer valor do teclado: ")
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
print("{} é: {}{}{}\n{}{}{}\n{}{}{}\n{}{}{}".format(n, cores['blue'], type(n), cores['limpar'],
                                                    cores['cian'], n.isnumeric(), cores['limpar'],
                                                    cores['purple'], n.isalpha(), cores['limpar'],
                                                    cores['gray'], n.isalnum(), cores['limpar']))
