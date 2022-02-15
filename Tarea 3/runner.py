import funciones

print("\n \n\n1.Círculo.\n2.Triángulo.\n3.Rectángulo.\n")

x=int(input("Elija de qué figura quiere calcular el área: "))

if x==1:

    radio=int(input('Ingrese el radio del circulo: '))
    funciones.area_circulo(radio)
    
if x==2:
    
    base1=int(input('Ingrese la base del triángulo: '))
    h1=int(input('Ingrese la altura del triángulo: '))
    funciones.area_triangulo(base1,h1)
   
    
if x==3:
    
    base2=int(input('Ingrese la base del rectángulo: '))
    h2=int(input('Ingrese la altura del rectángulo: '))
    funciones.area_rectangulo(base2,h2)
    
