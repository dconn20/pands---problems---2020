# Damien Connolly
# A program that outputs whether or 
# not today is a weekday. 



import datetime
import calendar


Day = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday" , 4:"Friday", 5:"Saturday", 6:"Sunday"}

now = datetime.datetime.today().weekday()
weekend = (5, 7)

if now == weekend:
    print ("Today is", Day[now], "the Weekend")
else:
    print ("Today is", Day[now], "a weekday")