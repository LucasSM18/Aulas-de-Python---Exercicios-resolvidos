n = int(input('Digite um número para ver sua tabuada: '))
for i in range(0, 11):
    print('{} x {} = {}'.format(n, i, n*i))