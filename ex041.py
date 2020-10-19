from datetime import date
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - ano
anoAlist = ano + 18
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade > 18:
    print('Você já deveria ter se alistado há {} ano(s).'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(anoAlist))
elif idade < 18:
    print('Ainda falta(m) {} ano(s) para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}'.format(anoAlist))
else:
    print('Você deve se alistar imediatamente!')

