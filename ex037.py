print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
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
if a+b > c and a+c > b and b+c > a:
    print(cores['blue'])
    print('Os segmentos acima PODEM formar um triângulo')
    print(cores['limpar'])
else:
    print(cores['red'])
    print('Os segmentos acima NÃO PODEM formar um triângulo')
    print(cores['limpar'])