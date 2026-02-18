edad = 18
print('edad:', edad)

altura = 1.68
print('altura:', altura)

complex_number = 3 + 1j
print('complex_number:', complex_number)

print('Area de un triangulo')
base = float(input('Agrega la base del triangulo:'))
altura = float(input('Agrega la altura del triangulo:'))
area = 0.5 * base * altura
print('El area del triangulo es:', area)

print('Perimetro de un traingulo')
a = float(input('Lado a:'))
b = float(input('Lado b:'))
c = float(input('Lado c:'))
perimetro = a + b + c
print(perimetro)

print('Area de un rectangulo')
lrg = float(input('Largo del rectangulo:'))
anc = float (input('Ancho del rectangulo:'))
area_rect = lrg * anc
print('El area es:', area_rect)
print('Perimetro del rectangulo:')
lar = float(input('Largo del rectangulo:'))
ach = float(input('Ancho del rectangulo:'))
peri = (lar + ach) * 2
print('El perimetro es:', peri)

print('Area de un circulo:')
rd =  float(input('Ingrese el radio:'))
ar= (rd ** 2) * 3.14
print('El area es:', ar)
print('Circunferencia de un circulo')
rad = float(input('Ingrese el radio:'))
circ = 2 * 3.14 * rad
print('La circunferencia es:', circ)

print('Pendiente de y=2x-2')
y2, y1 = -2, 0
x2, x1 = 0, 1
m= (y2 - y1) / (x2 - x1)
print('La pendiente es:', m)

print('Pendiente y distancia euclidea de (2, 2) y (6, 10)')
y_2, y_1 = 10, 2
x_2, x_1 = 6, 2
m_1 = (y_2 - y_1) / (x_2 - x_1)
print('La pendiente es:', m_1)
print('Distancia euclidea')
de = (((x_2 - x_1)**2 + (y_2 - y_1)**2)** 0.5)
print('La distancia euclidea es:', de)

print(m == m_1)

x = -3
y = (x ** 2) + (6 * x) + 9
print('Cuando x es (-3), el valor de y es:', y)

print(len('python') == len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')

print('jargon' not in 'I hope this course is not full of jargon')

lng= len('python')
pht = 'python'
lgt = len(pht) 
lflt = float(lgt)
print(lflt)
lstr = str(lgt)
print(lstr)

numero = int(input('Introduce un numero:'))
if numero % 2 == 0:
    print('El numero es PAR')
else:
    print('El numero es IMPAR')

print(7/3 == 2.7)

print('10' == 10)

paso1 = float('9.8')
paso2= int(paso1)
print('El valor final es:', paso2)
print('¿Es igual a 10?', paso2 == 10)

iht = float(input('Introduce horas trabajadas:'))
htr = float(input('Introduce tarifa por hora:'))
todo = iht * htr
print('Tu salario semanal es:', todo)

años = float(input('Introduce cuantos años has vivido:'))
año = años * 31536000
print(f'Has vivido {año} segundos')

print('1 1 1 1 1')
print(f'2 1 2 {2**2} {2**3}')
print(f'3 1 3 {3**2} {3**3}')
print(f'4 1 4 {4**2} {4**3}')
print(f'5 1 5 {5**2} {5**3}')



