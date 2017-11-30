#Calcular area cuadrado

def calcularAreaCuadrado(l1,l2):
    area = l1 * l2
    return area
lado1 = int(input("Ingrese lado1: "))
lado2 = int (input("Ingrese lado2: "))
areaCu = calcularAreaCuadrado(lado1,lado2)
print("La area del cuadrado es: "+str(areaCu))

def area_Rectangulo():
    print('AREA RECTANGULO')
    base = float(input('Ingrese valor de la base del rectangulo'))
    altura = float(input('Ingrese valor de la altura del rectangulo'))
    area = base * altura
    print('El area del rectangulo es: ' + str(round(area, 2)))

def calcularAreaTriangulo(b,a):
    areaTriangulo = (b * a) / 2
    return areaTriangulo

base = int (input("Ingrese la base del triangulo en metros:\n"))
altura = int (input("Ingrese la altura del triangulo en metros:\n"))
areaTriangulo = calcularAreaTriangulo(base,altura)
print("El area del triangulo es: "+str())

area_Rectangulo()
