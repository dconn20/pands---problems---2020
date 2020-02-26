# Damien Connolly
# Write a program that asks the user to input any positive integer
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.


Y = int(input( "Enter Numer: "))
Z = 2

while Y > 1:
    if Y % Z == 0:
        Y /= 2
        print (Y,end= '') 

    else:
        Y = (Y * 3) + 1
        print (Y,end= '')