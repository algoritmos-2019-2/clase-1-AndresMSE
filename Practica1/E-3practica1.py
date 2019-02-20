#Un ciclo que imprima los primeros M números impares.

print("Los M números impares son los siguientes")
cuenta = 0
i = int(input("¿Cuál es el M número?"))
for k in range(i):
	if k % 2 != 0:
		cuenta = cuenta + 1
print(f"Desde 1 hasta {i} hay {cuenta} números impares")
