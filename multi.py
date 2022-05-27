a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = 1
d = int(input("Veces a multiplicar: "))
e = 0

print()

ca = []
cb = []

while (c < d):
	ca.append(a * c)
	cb.append(b * c)
	c = c + 1

for h in ca:
	for j in cb:
		if (j == h):
			if (e == 0):
				e = j
				print(f"El minimo comun multiplo (MCM) es: {j}")
			else:
				print(f"Otros multiplos en común {j}")