print("Factorial")
prod = 1
print("Escribe un número")
n = int(input())
print(str(n) + "!es:")
for i in range(n):
	prod = prod * (i + 1)
print(prod)
