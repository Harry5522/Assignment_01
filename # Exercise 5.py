# Exercise 5

Month = { #here i write the day months 

   1: 31,
   2: 28,
   3: 31,
   4: 30,
   5: 31,
   6: 30, 
   7: 31, 
   8: 31, 
   9: 30, 
   10: 31, 
   11: 30, 
   12: 31, 
}


usermonth = int(input("Enter the Month number: "))  # asks the user to writer which month he wants.
if usermonth in Month:                     # if what is displayed in usrename is in Month print()
   print(f"{Month[usermonth]}")


#A07


