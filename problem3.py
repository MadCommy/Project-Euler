# What is the largest prime factor of the number 600851475143 ?
u
p = 1
n = 600851475143
while p <= n:
    p += 1
    while n % p == 0:
        n = n / p
print(p)
