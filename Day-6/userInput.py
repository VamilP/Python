# Write a program that uses a while loop to keep asking the user for input until they enter the word “stop”.

while True:
    userInput = input("Enter a word or write stop to exit: ").lower()
    if(userInput == "stop"):
       break
    else:
        print(f"You entered: {userInput}")