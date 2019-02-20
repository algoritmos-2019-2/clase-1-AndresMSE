#Escribe un programa corto que imprima los primeros "N" números y la suma de mismos "N" usando un bucle for.

print("Primeros N números y su suma")


i = 1
suma = 0 
while i < 11: 
	suma = suma + i 
	i = i + i
	print(f"La suma es {suma}")

print("Fin del programa")

