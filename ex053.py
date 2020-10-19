print('='*50)
print('{:15}10 TERMOS DE UMA PA'.format(' '))
print('='*50)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print('{}'.format(i), end=' -> ')
print('FIM')