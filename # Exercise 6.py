# Exercise 6

password = 123450
M_Attempts = 5    # Number of attempts remaining
Attempts = 0      # The value at which the count of attempts will begin.


# WE Use While to if the user inter the correct password before the maximum number of attempts
# He is allowed to Access
while Attempts < M_Attempts:
    User = input("Enter the Passowrod:")

    if User == password:
        print("You have access")
        break 
    else:
         Attempts += 1 # After each wrong attempt, one attempt is counted.
    R_Attempts = M_Attempts - Attempts
     #A mathematical operation that subtracts the maximum number of attempts
     #from the number of attempts made to find the number of attempts remaining.

    if R_Attempts > 0:
        print ("Invalid password. Number of attempts remaining:", + (R_Attempts)) 
    else:
        print("You have reached the maximum number of trys. The user will be notified.")

#A07