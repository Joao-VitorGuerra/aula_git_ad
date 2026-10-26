numero = int (input("Insira um número"))

if numero % 3 == 0:
	print ("Fizz")
	
elif numero % 5 == 0:
	print("Buzz")
	
elif numero % 15 == 0: 
	print("FizzBuzz")
	
else: print (numero)