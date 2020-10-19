distancia = float(input('Qual a distância, em Km, da sua localização até o seu destino? '))
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45   #if simplificado
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
print('O preço de uma viagem de {}{}{}Km será de {}R${:.2f}{}'.format(cores['green'], distancia, cores['limpar'], cores['green'], preco, cores['limpar']))