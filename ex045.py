
p = float(input('Qual é o seu peso? (kg) '))
h = float(input('Qual é a sua altura? (m) '))
imc = p/(h ** 2)
print('O ICM dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal!')
elif 18.5 <= imc < 25:
    print('Você está com o peso IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO, fique em alerta!')
elif 30 <= imc < 40:
    print('Você sofre com OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você sofre com OBESIDADE MÓRBIDA, cuidado!')