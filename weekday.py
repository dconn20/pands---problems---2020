# Write a program that outputs whether or 
# not today is a weekday. 
# An example of running this program on a 
# Thursday is given below.


import datetime
import calendar

L={0:"Monday", 1:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}

now = datetime.datetime.now()
day = now.weekday
weekend = (5, 7)

if day < weekend
    print ("Today is a week day")
    else:
        print ("Weekend")