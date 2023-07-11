import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

listItems = [rock, paper, scissors]

humanChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if(humanChoice >=3 or humanChoice <0):
    print("Invalid entry, You lose!")
else:

    print("You choose:\n")
    print(listItems[humanChoice])

    computerChoice = random.randint(0,2)
    print("Computer choose:\n")
    print(listItems[computerChoice])


    if(humanChoice == 0 and computerChoice == 2):
        print("You win!")

    elif(computerChoice > humanChoice):
        print("You lose!")

    elif(humanChoice > computerChoice):
        print("You win!")

    elif(humanChoice == computerChoice):
        print("It's a draw.")

