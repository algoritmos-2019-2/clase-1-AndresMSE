#Escriba un programa que calcule los primeros N términos de la serie de fibonacci.

print("Serie de N número de Fibonachi")

n = int(input("Define N"))
print(f"Los primeros {n} números de la serie de fibonachi :")
k = [1,1]
serie = 0 
if n == 1:
	print(1)
else:
		while len(k) < n:
			serie = k[-1] + k[-2]
			k.append(serie)
			print(k)
print("")


 
