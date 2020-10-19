from colorama import Style, Fore
style = Style.RESET_ALL
print("=" * 10, end='')
print('{:=^40}'.format('LOJAS MISSALIA'), end='')
print("=" * 10)
preco = float(input('Preço das compras: '))
opcao = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 4x ou mais no cartão
Qual é a opção? '''))
if opcao == 1:
    total = preco - (preco * 0.1)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    valor = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(valor))
elif opcao == 4:
    total = preco + (preco * 0.2)
    totparcela = int(input('Quantas parcelas?\n'))
    parcela = total / totparcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totparcela, parcela))
else:
    total = preco
    print('{}OPÇÃO INVÁLIDA de pagamento!{}'.format(Fore.RED, style))
    exit()
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))