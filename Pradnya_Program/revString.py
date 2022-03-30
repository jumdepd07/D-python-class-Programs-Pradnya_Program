A = 'Python'
List1 = []
for s in A:
    List1.append(s)
print(List1)
List2 = []

i = len(List1)-1
while(i>=0):
    List2.append(List1[i])
    i = i-1
print(List2)

B = ''.join(List2)
print(B)

