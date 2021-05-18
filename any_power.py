def firse():
      n= int(input('Enter Number : '))
      power= int(input('Enter the number of powers:'))
      print(n**power)

      restart = input("Would you like to restart this program? ")
      if restart == "yes" or restart == "y":
        firse()
      if restart == "n" or restart == "no":
        print ("Script terminating. Goodbye.")
      
firse()
