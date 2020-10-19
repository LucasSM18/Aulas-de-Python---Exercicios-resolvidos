sum = 0
maior = 0
count = 0
N = ''
for i in range(1, 5):
    print('-'*5, end=' ')
    print('{}° PESSOA'.format(i), end='')
    print('-' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')[0]).strip()
    sum += idade
    if sexo in 'Mm' and idade > maior:
        maior = idade
        N = nome
    elif sexo in 'Ff' and idade < 20:
        count += 1
media = sum/4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, N))
print('Ao todo são {} mulheres com menos de 20 anos'.format(count))