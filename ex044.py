print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a+b > c and a+c > b and b+c > a:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')


