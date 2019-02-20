#Escriba una rutina que genere todas las tablas de verdad de cada operador booleano (es decir, cada combinación posible de valores booleanos para cada  operador). 

print("Tablas de Verdad")
a=[True, False]
b=[True, False]

print("Tabla AND")
for i in a:
	for k in b:
		print(i,k, i and k)
print()

print("Tabla NOT")
for i in a:
	print(i, not i)
print()

for k in b:
	print(k, not k)
print()


print("Tabla OR")
for i in a:
	for k in b:
		print(i,k, i or k)
print()

