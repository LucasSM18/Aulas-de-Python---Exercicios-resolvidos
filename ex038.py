v = float(input('Qual o valor da casa? R$'))
s = float(input('Quanto você ganha? R$'))
a = int(input('Você quer financiar em quantos anos? '))
p = v/(a*12)
m = s * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(v, a, p))
if p <= m:
    print('Empréstimo Concedido!')
else:
    print('Empréstimo Negado!')