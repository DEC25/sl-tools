indice = input("Elija un indice (r = rentabilidad/l = liquidez/s = solvencia/g = generales): ").lower()
print()
if indice == "r":

    dato = input("Metodos (g = ganancia / t = total): ").lower()
    print()

    if dato == "g":
        print("Ingrese los datos:")
        print()
        ub = float(input("Utilidad Bruta: "))
        v = float(input("Ventas: "))

        result = (ub/v)*100
        print()
        print(f"El resultado es: {result}%")

    elif dato == "t":
        print("Ingrese los datos:")
        print()
        ub = float(input("Utilidad Neta: "))
        v = float(input("Ventas: "))

        result = (ub/v)*100
        print()
        print(f"El resultado es: {result}%")

elif indice == "l":
    print("Ingrese los datos:")
    print()
    ub = float(input("Utilidad Bruta: "))
    v = float(input("Ventas: "))

    result = (ub/v)*100
    print()
    print(f"El resultado es: {result}%")



"""def calculo(nombre, div1, div2):
    result = div1 / div2
    print()
    print(f"{nombre} es:  {result}")

nom = input("Nombre: ")
div = float(input("Div: "))
divi = float(input("div: "))
calculo(nom, div, divi)"""