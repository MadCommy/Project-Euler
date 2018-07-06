# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
sum = 0
x = 1
y = 2
n = 0
while y <= 4000000:
    if y%2 == 0:
        sum += y
    n = x + y
    x = y
    y = n
print(sum)
