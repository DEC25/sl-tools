def sintesis():
    operacion = input("¿Que operacion desea realizar? (FSC, FSA, FCS, FDFA, FAS, FRC): ").lower().strip()
    print()

    if operacion == "fsc":
        print("Escriba los datos '(1 + i)^n)' :")
        print()
        monto = float(input("Ingrese el monto: "))
        i = float(input("Valor de i (porcentaje): ")) / 100
        n = float(input("Valor de n (años): ")) 

        solucionT = (monto * ((1 + i)**n))
        solucion = round((monto * ((1 + i)**n)), 2)
        print()
        print(f"La solucion es : {solucion}")
        print()
        print(f"Solucion Total : {solucionT}")

    elif operacion == "fsa":
        print("Escriba los datos '1 /(1 + i)^n)' :")
        print()
        monto = float(input("Ingrese el monto: "))
        i = float(input("Valor de i (porcentaje): ")) / 100
        n = float(input("Valor de n (años): ")) 

        solucionT = (monto * (1 / ((1 + i)**n)))
        solucion = round((monto * (1 / ((1 + i)**n))), 2)
        print()
        print(f"La solucion es : {solucion}")
        print()
        print(f"Solucion Total : {solucionT}")

    elif operacion == "fcs":
        print("Escriba los datos '((1 + i)^n) - 1) / i' :")
        print()
        monto = float(input("Ingrese el monto: "))
        i = float(input("Valor de i (porcentaje): ")) / 100
        n = float(input("Valor de n (años): "))

        solucionT = monto * ((((1 + i)**n) - 1) / i)
        solucion = round(monto * ((((1 + i)**n) - 1) / i), 2)
        print()
        print(f"La solucion es : {solucion}")
        print()
        print(f"Solucion Total : {solucionT}")

    elif operacion == "fdfa":
        print("Escriba los datos 'i / ((1 + i)^n) - 1)' :")
        print()
        monto = float(input("Ingrese el monto: "))
        i = float(input("Valor de i (porcentaje): ")) / 100
        n = float(input("Valor de n (años): ")) 

        solucionT = (monto * (i / (((1 + i)**n) - 1)))
        solucion = round((monto * (i / (((1 + i)**n) - 1))), 2)
        print()
        print(f"La solucion es : {solucion}")
        print()
        print(f"Solucion Total : {solucionT}")

    elif operacion == "fas":
        print("Escriba los datos '((1 + i)^n) - 1) / i(1+i)^n' :")
        print()
        monto = float(input("Ingrese el monto: "))
        i = float(input("Valor de i (porcentaje): ")) / 100
        n = float(input("Valor de n (años): ")) 

        solucionT = (monto * ((((1+i)**n)-1) / (i * ((1+i)**n))))
        solucion = round((monto * ((((1+i)**n)-1) / (i * ((1+i)**n)))), 2)
        print()
        print(f"La solucion es : {solucion}")
        print()
        print(f"Solucion Total : {solucionT}")
        
    elif operacion == "frc":
        print("Escriba los datos ' i(1+i)^n / ((1 + i)^n) - 1)' :")
        print()
        monto = float(input("Ingrese el monto: "))
        i = float(input("Valor de i (porcentaje): ")) / 100
        n = float(input("Valor de n (años): ")) 

        solucionT = (monto *((i * (1+i)**n) / (((1 + i)**n) - 1)))
        solucion = round((monto *((i * (1+i)**n) / (((1 + i)**n) - 1))), 2)
        print()
        print(f"La solucion es : {solucion}")
        print()
        print(f"Solucion Total : {solucionT}")

    else:
        print("El nombre es invalido, elija una coincidencia")
        print()
        sintesis()

    continuar()

def continuar():
    print()
    res = input("¿Desea hacer otra operacion? (y/n) : ").lower().strip()

    if res == "y":
        print()
        sintesis()
    elif res == "n":
        print()
        print("########## Gracias por usar el programa! ##########")
    else:
        print()
        print("Respuesta invalida, ingrese una coincidencia")
        continuar()


sintesis()