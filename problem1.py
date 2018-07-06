# Find the sum of all the multiples of 3 or 5 below 1000.
numbers = []
i = 0
j = 0
while i < 1000:
    i += 3
    numbers.append(i)
    j += 5
    numbers.append(j)


numbers = list(set(numbers))
total = sum(numbers)
print(total)
