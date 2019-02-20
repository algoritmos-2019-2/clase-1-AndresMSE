print("Tablas de Verdad")
while True:
	print("Which Boolean?")
	boolean = input()
	if boolean != "AND":
		continue
	print("Boolean AND?")
	answer = input()
	if answer == "yes":
		break
print("Set variable x")
x = input()
print("Set variable y")
y = input()
if x == y:
	print("TRUE")
elif x != y:
	print("FALSE")

