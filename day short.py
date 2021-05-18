year = int(input("Enter year:  "))
a= year-1900
if (a)%4==0:
	leap_1= a/4
elif  (a)%4 != 0:
	leap_1= int(a/4)
day = int(input("Enter the Date: "))
print(">>>>>>>>Jan and Oct- 1")
print("Feb , March and Oct- 4")
print(" >>>April and July - 0")
print(" >>>>>>>>>>>>>>>May- 2")
print(" >>>>>>>>>>>>>>June- 5")
print(" >>>>>>>>>>>>August- 3")
print(" >>>>> Sept and Dec- 6")
print("")
month= input("Choose code according to the month: ")

Sum= int(a) + int(leap_1) + int(day) +int(month)
rem= (Sum)%7
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




