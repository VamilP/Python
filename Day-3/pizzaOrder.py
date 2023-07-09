print("Welcome to Pizza Deliveries")

size = input("What size pizza do you want? S, M, or L:\n")
addPepperoni = input("Do you want pepperoni? Y or N:\n")
extraCheese = input("Do you want extra cheese? Y or N:\n")


if(size == "S"):
    if(addPepperoni == "Y"):
        bill = 17
    else:
        bill = 15

elif(size == "M"):
    if(addPepperoni == "Y"):
        bill = 23
    else:
        bill = 20
    
elif(size == "L"):
    if(addPepperoni == "Y"):
        bill = 28
    else:
        bill = 25
    
if(extraCheese == "Y"):
    bill += 1

print(f"Your final bill is ${bill}.")