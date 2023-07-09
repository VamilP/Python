print("Welcome to Love Calculator")

name1 = input("What is your name?\n")
name2 = input("What is your name?\n")

combinedName = name1 + name2

lowerCaseName = combinedName.lower()

t = lowerCaseName.count("t")
r = lowerCaseName.count("r")
u = lowerCaseName.count("u")
e = lowerCaseName.count("e")

true = t+r+u+e

l = lowerCaseName.count("l")
o = lowerCaseName.count("o")
v = lowerCaseName.count("v")
e = lowerCaseName.count("e")

love = l+o+v+e

combinedString = int(str(true) + str(love))


if combinedString <10 and combinedString >90:
    print(f"Your score is {combinedString}, you go together like coke and mentos.")

elif combinedString >=40 and combinedString <=50:
    print(f"You score is {combinedString}, you are alright together.")

else:
    print(f"Your score is {combinedString}.")