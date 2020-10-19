n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
# verificando quem é o menor
menor = n1
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
if n2 < menor and n2 < n3:
    menor = n2
elif n3 < menor and n3 < n2:
     menor = n3
# verificando quem é o maior
maior = n1
if n2 > maior and n2 > n3:
    maior = n2
elif n3 > maior and n3 > n2:
    maior = n3
print('\nO menor valor digitado foi {}{}{}'.format(cores['red'], menor, cores['limpar']))
print('O maior valor digitado foi {}{}{}'.format(cores['red'], maior, cores['limpar']))