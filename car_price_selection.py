#For selection of price 
print( "Which car do you want for Rent? ")
print("A= Audi"
        "  B = Creata "
         " C = BMW")
choosen_car = input('Which one : ')

ride_price = 0
if choosen_car == "A" or choosen_car == "a":
	ride_price = 30000
	print(f"Rupess {ride_price}")
elif choosen_car == "B" or choosen_car == "b":
	ride_price = 15000
	print(f"Rupess {ride_price}")
else:
	ride_price = 50000
	print(f"Rupees {ride_price}")
	