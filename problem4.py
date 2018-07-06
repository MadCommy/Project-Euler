# Find the largest palindrome made from the product of two 3-digit numbers.
largest = 0
c = 0
x = 0
y = 0
for a in range (100,1000):
    for b in range(a,1000):
        c = a * b
        s = int (str (c)[::-1])
        if s == c and s > largest:
            largest = s
            x = a
            y = b
print(largest)
