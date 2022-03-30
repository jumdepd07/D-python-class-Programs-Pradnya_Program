def calc(a,b,c=0):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    print("c=",c)
    return sum,sub,mul,div
addition,subtraction,multiplication,divsion=calc(a=100,b=50)

print("The Results are")
#l = ['addition','subtraction','multiplication','divsion']
#for i in t:
print("sum =",addition,'subtraction =',subtraction)