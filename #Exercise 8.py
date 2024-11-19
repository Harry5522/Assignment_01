#Exercise 8

Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]   #Yhis is a list we creat
User = input(str("Enter the Name:"))
if User in Names:                       # This means that if the user entered it is present in the variable name,
                                        # the string will be printed in If, else.
    print(f"Yes, {User} is on the list.")     # i use 'f' to write the things in order
else:
    print(f"Sorry, {User} is not on the list.")  


#A07