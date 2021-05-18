points = int(input("Enter Earned Points: "))
points_needed = 1000
Name = input("Enter your Name: ")
if points >= points_needed:
	
	print("Congrats",Name, "you are on level 2")
else :
		Left = points_needed - points
		print("Sorry " ,Name, "you need", Left,"more to reach level 2")
		
	