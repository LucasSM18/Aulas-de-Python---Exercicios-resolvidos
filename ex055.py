frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
juntar = ''.join(palavra)
inverso = juntar[::-1]
print('O inverso de {} é {}'.format(juntar, inverso))
if juntar == inverso:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
