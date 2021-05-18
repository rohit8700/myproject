data_1 = int(input("Length + or -  percent change: "))
data_2 = int(input("Breadth + or - percent change: "))
change  = 0
change_2 = 0
total_change= 0


if data_1< 0:
	percent= (data_1)/10
	change= 10 + percent
	
elif data_1 >0:
	percent= (data_1)/10
	change= 10 + percent
	
if data_2 < 0:
	percent_2= (data_2)/10
	change_2= 10 + percent_2
	
elif data_2> 0:
	percent_2 = (data_2)/10
	change_2= 10 + percent_2

total_change = change * change_2
print(f"The change in percentage is: {total_change}")
inc= total_change - 100

if inc < 100:
	print(f"Wow! There is { inc } percent increase in the Area")
elif inc > 100:
	print("Ohhh !! There is {  inc } percent decrease in Area")
	
	
	
	

