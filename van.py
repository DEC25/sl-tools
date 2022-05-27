van = 0
inver = int(input("Ingresa la inversion inicial: "))
van -= inver

per = int(input("Efectivo por periodo: "))

porcent = int(input("Ingresa el porcentaje: "))
porc = porcent / 100


años = int(input("Ingresa los años: "))

k = 1

while(k<años+1):
    periodo = (per / (1+porc)**k)
    van += periodo
    k = k+1

print()
print(f"El valor es {round(van, 2)}")
