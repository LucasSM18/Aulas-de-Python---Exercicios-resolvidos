s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
        c += 1
print('A soma de todos os {} valores solicitados é {}'.format(c, s))