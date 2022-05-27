def error_Div(ndiv):

    print()
    s = ndiv

    if s == 0:
        while s == 0:

            print("La division entre 0 es indefinida, pruebe otro numero")
            print()
            s = float(input("Escribe el dividendo: "))
            print()
        
        return s
            
    else:
        return s


def Porcentaje():
    print()
    print("Ingresos en los respectivos años a comparar:")
    print()
    numero1 = float(input("Año actual: ").replace(",", "")) ##510
 
    numero2 = float(input("Año anterior: ").replace(",", "")) ##500

    ndiv = numero2

    div = error_Div(ndiv)

    result = (numero1 - numero2) / div

    porc = result * 100

    for c in str(porc):
        if c[0] == "-":
            print("Disminuyó " + str(round(porc, 2)) + "%")
            print()
            break
        else:
            print("Aumentó " + str(round(porc, 2)) + "%")
            print()
            break
    
    continuar()
    

def continuar():
    cont = input("¿Desea continuar? (y/n): ").lower()
    print()

    if cont == "y":      
        print("---------------------------- Nuevos datos ----------------------------")
        Porcentaje()
    elif cont == "n":
        print()
        print("Gracias por usar el programa!")
        print()
    else:
        print("La respuesta es invalida")
        print()
        continuar()


Porcentaje()