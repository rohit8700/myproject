marks = float(input('How much marks you got:'))
total_marks = int(input('Out of: '))
percentage_1 =(marks*100)/total_marks

if percentage_1 <33:
	print("Soryy You Failed in Examination,,😞 ")
	print("You got ",percentage_1)
elif percentage_1 <=100:
	print("Hurray You passed the examination")
	print("You got", percentage_1)
	