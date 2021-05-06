reta_um = float(input('Digite o tamanho da reta1: '))
reta_dois = float(input('Digite o tamanho da reta2: '))
reta_tres = float(input('Digite o tamanho da reta3: '))

if reta_um > reta_dois > reta_tres and reta_dois < reta_um > reta_tres and reta_tres < reta_dois < reta_um:
    print('Eh possível formar um triangulo :D .')
elif reta_dois > reta_um > reta_tres and reta_um < reta_dois > reta_tres and reta_tres < reta_um < reta_dois:
    print('Eh possivel criar um triangulo :D .')
elif  reta_tres > reta_dois > reta_um and reta_um < reta_tres > reta_dois and reta_um < reta_dois < reta_tres:
    print('Eh possivel criar um triangulo :D .')
else:
    print('ENão eh possível formar um triangulo.')