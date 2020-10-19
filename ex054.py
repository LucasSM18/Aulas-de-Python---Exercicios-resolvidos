from colorama import Fore, Style
fore = Fore.YELLOW
fore2 = Fore.RED
style = Style.RESET_ALL
num = int(input('Digite um número: '))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(fore, end='')
        count += 1
    else:
        print(fore2, end='')
    print(i, end=' ')
print('\n{}O número {} foi divisível {} vezes'.format(style, num, count))

if count == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')


