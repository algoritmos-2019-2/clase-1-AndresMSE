#Escribe un programa corto que imprima los primeros "N" números y la suma de mismos "N" usando un bucle for.

print("Primeros N números y su suma")

i = int(input("¿Cuántos números quiere sumar?"))
suma = 0
for k in range(1,i):
	suma = suma + k
	print(f"Voy en el número {k}")
	print(f"La suma es {suma}")

print("Fin del programa")
		
