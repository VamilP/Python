student_heights = input("Enter a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
count = 0

for height in student_heights:
    sum += height

print(sum)

for student in student_heights:
    count += 1

print(count)

averageHeight = round(sum/count)
print(f"Average Height is {averageHeight}")