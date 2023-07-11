<<<<<<< HEAD
import random

namesString = input("Give me everybody's names, separated by a comma:\n")

names = namesString.split(",")

totalItems  = len(names)
randomChoice = random.randint(0, totalItems-1)
listNames = names[randomChoice]

print(f"{listNames} is going to buy the meal today!")

=======
import random

namesString = input("Give me everybody's names, separated by a comma:\n")

names = namesString.split(",")

totalItems  = len(names)
randomChoice = random.randint(0, totalItems-1)
listNames = names[randomChoice]

print(f"{listNames} is going to buy the meal today!")

>>>>>>> d28f67691b5116b42ffbc9c7fdd3a61e85d33450
# listNames = random.choice(names)