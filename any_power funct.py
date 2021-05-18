user = int(input('Enter the number:  '))
power = int(input('Enter number of powers: '))
def square(user):
	result= user**power
	return result
square(user)
print(square(user))