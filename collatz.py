# Damien Connolly
# Write a program that asks the user to input any positive integer
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.


Pos = int(input( "Enter Number: "))
Z = 2

while Pos > 1:
    if Pos % Z == 0:
        Pos /= 2

    else:
        Pos = (Pos * 3) + 1
        

    print (Pos,end= '')