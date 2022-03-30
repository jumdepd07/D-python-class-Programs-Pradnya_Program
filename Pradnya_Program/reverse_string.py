s1 = input("print any string")
l1 = []
for i in s1:
    if i not in l1:
        l1.append(i)
        #print(i)

S2 = ''.join(l1)
print(f"s2: {S2}")