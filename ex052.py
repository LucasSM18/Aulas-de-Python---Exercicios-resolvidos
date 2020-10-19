sum = 0
cont = 0
for i in range(0, 6):
    num = int(input('Digite o {}° número: '.format(i + 1)))
    if num % 2 == 0:
        sum += num
        cont += 1
print('A soma de todos os {} números PARES é: {}'.format(cont, sum))
