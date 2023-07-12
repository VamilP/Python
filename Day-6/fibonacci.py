# Write a program that uses a for loop to print out the first 10 numbers of the Fibonacci sequence.

n = int(input("Enter a number for range: "))

#Using List

fib_sequence = [0, 1] 

for i in range(2, n):
    fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

for num in fib_sequence:
    print(num)

#Without using List

a, b = 0, 1

print(a)
print(b)

for _ in range(2, n):
    c = a + b
    print(c)
    a, b = b, c
