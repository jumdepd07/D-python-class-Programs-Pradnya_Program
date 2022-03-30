print("Write a Python function to sum all the numbers in a list")

#def SumList(*args):
#    sum = 0
#    if args:
#        sum = sum + args
#    return sum

#a = SumList([1,2,3,4,5])
#print(a)

def summation(numbers):
    total = 0
    for x in numbers:
        total = total +x
    return total
print(summation([1,2,3,4,5]))
print(summation([0,9,8,7,6]))