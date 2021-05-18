year_1= int(input("Year of the birth: "))
year= year_1-1900
leap_years= (year)/4
code= 0
if (year)%4 == 0:
	print()
month= input("Enter Month: ")
if month == "jan" or month== "oct":
	code= 1
elif month== "feb" or month== "march" or month== "nov":
	code= 4
elif month== "april" or month== "july":
	code= 0
elif month== "may":
	code= 2
elif month== "june":
	code=5
elif month=="august":
	code=3
elif month== "sept" or month== "dec":
	code=6

day= int(input("Enter the day: "))
total= year+ leap_years + code+ day

rem= (total)%7
if rem==1:
	print("Sunday")
elif rem==2:
	print("Monday")
elif rem==3:
	print("Tuesday")
elif rem==4:
	print("Wednesday")
elif rem==5:
	print("Thursday")
elif rem==6:
	print("Friday")
elif rem==0:
	print("Saturday")
