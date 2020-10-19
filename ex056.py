from datetime import date
atual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(i)))
    idade = atual - nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))

