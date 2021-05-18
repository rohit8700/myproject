operator = input('Enter opertor to perform: ')
x = float(input('Enter number: '))
y= float(input('Enter another number: '))

def calculator(operator, x, y):
	result = 0
	
	if operator== "+":
		result = x+y
		print(f"{x} {operator} {y} = { result}")
	elif operator == "-":
		result = x-y
		print(f"{x} {operator} {y} = { result}")
	elif operator== "*":
		result = x*y
		print(f"{x} {operator} {y} = { result}")
	elif operator== "/":
		result = x/y
		print(f"{x} {operator} {y} = { result}")
	elif operator== "%" :
		result = x%y
		print(f"{x} {operator} {y} = { result}")
		

calculator(operator, x, y)
	