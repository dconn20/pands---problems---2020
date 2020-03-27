# Damien Connolly
# A program that outputs whether or 
# not today is a weekday. 


import datetime
import calendar

Day = ("Monday", "Tuesday", "Wednesday", "Thursday" , "Friday", "Saturday", "Sunday")

now = datetime.datetime.today().weekday()
weekend = (5, 7)

if now == weekend:
    print ("Today is", Day[now], "the Weekend")
else:
    print ("Today is", Day[now], "a weekday")