#import math
def factor(num):
    result = 1
    while num >=1:
        result = result*num
        num = num -1
    return result

number = int(input("enter number"))
print("factorial of",number,"is",factor(number))

