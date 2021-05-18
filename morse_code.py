def code_change(code):
   code = code.replace("1",".---------")
   code = code.replace("2","..--------")
   code = code.replace("3","...-------")
   code = code.replace("4","....------")
   code = code.replace("5",".....-----")
   code = code.replace("6","......----")
   code = code.replace("7",".......---")
   code = code.replace("8","........--")
   code = code.replace("9",".........-")
   code = code.replace("0","..........")
       
   return code
enter = input("Enter the numbers: ")
		
morse = code_change(enter)
print(f"Morse code is : {morse}")
#program ends


		
