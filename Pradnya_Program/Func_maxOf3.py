print("Program to find maximun number out of three numbers")
def maximum(num1,num2,num3):
#    num1 = float(input("enter number1"))
#    num2 = float(input("enter number2"))
#    num3 = float(input("enter number3"))
    if num1 > num2:
        if num1 > num3:
            print(f"{num1} is maximum number")
            return num1
        elif num1 < num3:
            print(f"{num3} is maximum number")
            return num3
        else:
            print(f"number1 and number3 is same having value {num1} which is maximum number ")
            return num1
    elif num1 < num2:
        if num2 > num3:
            print(f"{num2} is maximum number")
            return num2
        elif num2 < num3:
            print(f"{num3} is maximum number")
            return num3
        else:
            print(f"number2 and number3 is same having value {num2} which is maximum number ")
            return num2
    else:
        if num1 > num3:
            print(f"number1 and number2 is same having value {num1} which is maximum number")
            return num1
        else:
            print(f"{num3} is maximum number")
            return num3

c= maximum(50,10,20)
print(c)