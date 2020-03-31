# Damien Connolly
# A funtion to square numbers


n = float(input("enter a positive number "))

def sqrt(n): 
    
    ans = n ** (1/2)
    print ("The square root of the number is", ans,)
    return ans
    

sqrt(n)


def newsq(number):
    x = int(number)
    for i in range(number):
        number = (number + x / number) ** (1/2) 
        print(number)
        return number
        

newsq(16)