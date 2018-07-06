# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 2 3 4   5 6   7 8   9   10  11 12    13 14  15  16  17 18    19 20
# 2 3 2^2 5 2*3 7 2^3 3^2 2*5 11 2^2*3 13 2*7 3*5 2^4 17 2*3^2 19 2^2*5

# 22222 33 5 77 11 13 17 19
n = (2^5) * (3^2) * (5) * (7^2) * (11) * (13) * (17) * (19)
print(n)
