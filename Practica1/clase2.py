while True:
	print("Who are you?")
	name = input()
	if name != "Joe":
		continue
	print("Hello, Joe. What is the password (It is a fish)")
	password = input()
	if password == "swordfish":
		break
print("Access granted")

l = [1,0.1,"Cadena", True, [2,3]]

print(type(l)," ",1)	
for i in l: 
	print(i)


