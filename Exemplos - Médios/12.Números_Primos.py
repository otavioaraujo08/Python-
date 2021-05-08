primo = int(input('Digite um valor:\n'))
tot = 0

for c in range(1, primo + 1):
    if primo % c == 0:
        print(f'O número {primo} eh divisivel por {c}.\n')
        tot += 1
    else:
        print(f'{primo} N EH DIVISIVEL POR {c}.\n')

if tot == 2:
    print(f'{primo} eh primo')
else:
    print(f'{primo} Não eh primo')