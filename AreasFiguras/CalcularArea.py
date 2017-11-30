

def CalcularAreas(n):
    if n == 1:

        def calcularAreaCuadrado(l1, l2):
            area = l1 * l2
            return area

        print("")
        lado1 = int(input("Ingrese lado1: "))
        lado2 = int(input("Ingrese lado2: "))
        areaCu = calcularAreaCuadrado(lado1, lado2)
        print("La area del cuadrado es: " + str(areaCu))

    elif n == 2:
        print("")
        def calcularAreaTriangulo(b, a):
            areaTriangulo = (b * a) / 2
            return areaTriangulo

        base = int(input("Ingrese la base del triangulo en metros: "))
        altura = int(input("Ingrese la altura del triangulo en metros: "))
        areaTriangulo = calcularAreaTriangulo(base, altura)
        print("El area del triangulo es: " + str(areaTriangulo))

    elif n == 3:

        def area_Rectangulo(base,altura):

            area = base * altura
            print('El area del rectangulo es: ' + str(round(area, 2)))
        print(" ")
        print('AREA RECTANGULO')
        base = float(input('Ingrese valor de la base del rectangulo: '))
        altura = float(input('Ingrese valor de la altura del rectangulo: '))
        areaRectan=area_Rectangulo(base,altura)

    elif n == 4:
        # Calcular area circulo
        def calcularAreaCirculo():

            area = 3.1416 * radio * radio
            print(area)
            return area

        radio = float(input("Ingrese el radio"))
        calcularAreaCirculo()

    else:
        print('')
        print('Inválido')



print("CALCULAR AREA" )
print("1. Calcular el area del cuadrado" )
print("2. Calcular el area del Triangulo" )
print("3. Calcular el area del Rectangulo" )
print("4. Calcular el area del Circulo" )
n = int(input("Ingrese el numero de seleccion: "))
CalcularAreas(n)