# Damien Connolly
# Check if a number is prime
# Prime numbers are 2, 3, 5, 7, 11, 13, ...

p = 676
m = 2
isprime = True

for m in range (2, p-1):
    if p % m ==0:
        isprime = False
    break 

if isprime:
    print (p, "is a prime number.")
else:
    print (p, "is not prime.")        