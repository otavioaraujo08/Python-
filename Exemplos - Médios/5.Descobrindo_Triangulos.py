lado_a = int(input('Valor do ângulo a:'))
lado_b = int(input('Valor do ângulo b:'))
lado_c = int(input('Valor do ângulo c:'))

if (lado_b - lado_c) < lado_a and  lado_a < (lado_b + lado_c):
    print('Triangulo formado')
elif (lado_a - lado_c) < lado_b and lado_b < (lado_a + lado_c):
    print('Triangulo Formado')
elif (lado_a - lado_b) < lado_c and lado_c < (lado_a + lado_b)  :
    print('Triangulo Formado')
else:
    print('Triângulo Pirata')

if lado_b == lado_a and lado_c == lado_a and lado_b == lado_c:
    print('\nVocê é um triangulo Equilatero.')
elif lado_a == lado_b or lado_a == lado_c or lado_c == lado_b:
    print('\nVocê é um triângulo Isósceles.')
else:
    print('\nVocê é um triângulo Escaleno.')