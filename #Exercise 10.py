#Exercise 10

def calculation(number):
    number = number % 2

    if number == 0:
       return "The number is even"

    else:
        return "The number is  odd"

def main():
    number = int(input("enter a number: "))
    print(f"{calculation(number)}")


main()















def main():
    even_odd = int(input("Enter the number: "))
    if even_odd % 2 == 0:
        print(f"{even_odd} is Even Number")
    else:
        print(f"{even_odd} is Odd Number")
        
if __name__ == "__main__":
    main()


    

    
