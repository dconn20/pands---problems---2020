# Damien Connolly
# Use to test codes.


a = int(input("Enter any positive integer number: "))
b = 2

print (a)

while a > 1:

    if a % b == 0:
        a /= 2
        print (a)
    
    else:
        a = (a * 3) + 1
        print (a)  
