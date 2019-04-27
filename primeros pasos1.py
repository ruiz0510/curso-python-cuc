# comentario de linea

import math

"""Comentario 
de parrafo
"""
# hola mundo

print("hello world")

# variables

x = 4
y = "Text"  # string
z = 4.5     # float
a = True    # booleano
b = False
c = 4+5j    # compleja

print(x, y, z, a, b, c)

# conocer el tipo de variable
print(type(c))

# conversiones de tipo de datos
# enteros
x = int(2.8)
print(x)
x = int("2")

# float
x = float(2)
x = float(2.8)
print(x)
x = float("2")

# string
x = str(2)
x = str(2.8)
print(x)
x = str("2")
# manejo de string en cadena de textos
bebe = "HELLO WORLD"
print(bebe[0])

bebe = bebe.strip()
print(len(bebe))
print(bebe.lower)
print(bebe.upper)

# operaciones

a = 2
b = 3
c = a + b
c = a - b
c = a * b
c = a / b   # cociente
c = a // b  # parte entera
c = a % b
c = a ** b  # exponente
c = math.sqrt(a)  # raiz
c = math.pi

# captura por consola

print("digite el nombre")
nombre = input()
print("hola"+nombre+"!")

print("digite el #1")
n1 = input()
n1 = float(n1)
print("digite el #2")
n2 = input()
n2 = float(n2)
print(n1+n2)

# condiciones

a = 5
b = 6

if a > b:
    print(a, "es mayor que", b)
else:
    print(b, "es mayor que", a)
    
if b > a :
    if b > 1:
        print(b, "es mayor que 1 y es mayor que", a)
        
 if a == b:
     print("son iguales")     
elif a > b:
    print(a,"es mayor que",b)
else:
    print(b,"es mayor que",a)

if a == b and a > 2:
    print(a,"es igual a",b,"mayor que 2")
        