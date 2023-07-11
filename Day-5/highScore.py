studentScores = input("Enter a list of students:\n").split()
for n in range(0, len(studentScores)):
    studentScores[n] = int(studentScores[n])
print(studentScores)

max = 0

for num in studentScores:
    if(num>max):
        max = num
print(f"The highest score in the class is: {max}")
