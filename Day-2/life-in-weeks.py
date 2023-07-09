age = int(input("What is your current age?\n"))

days = (90*365) - (age*365)
weeks = (90*52) - (age*52)
months = (90*12) - (age*12)

print(f"You have {days} days, {weeks} weeks and {months} months left.")