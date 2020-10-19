from random import shuffle
i = 0
Lista = []
while i < 4:
    a = input("Digite o nome do {}° aluno: ".format(i+1))
    Lista.append(a)
    i += 1;
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
shuffle(Lista) #Irá embaralhar a lista
print("A ordem da Apresentação dos trabalhos será:")
print(cores['blue'],Lista, cores['limpar'])