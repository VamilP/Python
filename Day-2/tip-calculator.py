print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? $"))
tipPercent = int(input("What percentage tip would you like to give? 10, 12, or 15 "))

billSplit = int(input("How many people to split the bill? "))


tip = totalBill * (tipPercent/100)
bill = totalBill + tip

finalBill = round((bill/billSplit),2)

print(f"Each person should pay: ${finalBill}")