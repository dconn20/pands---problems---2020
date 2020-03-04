# Damien Connolly
# A funtion to square numbers


#n = float(input("enter a positive number "))

def sqrt(n): 
    
    ans = n ** (1/2)
    print ("The square root of the number is", ans,)
    return ans
    

#sqrt(n)


def newsq(number, number_iters = 500):
    x = float(number)
    for i in range(number_iters):
        number = 0.5 * (number + x / number)
        print(number)
        return number
    #print(number)


newsq(9)