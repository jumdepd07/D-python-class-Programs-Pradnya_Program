
#i = 0
#j = 1
# print(len(l))
# for i in range(0,len(l)):
#     for j in range(1,len(l)):
#         print("j =", j)
#         if l[i] > l[j]:
#             a = l[i]
#             l[i] = l[j]
#             l[j] = a
#         #else:
#     print("i=",i)
#         #j = j+1
#     #i = i+1
# print(l)
l = [34, 0, -12, 45, 98, 9, 67]
l2 = []
while l:
    min = l[0]
    for x in l:
        if x < min:
            min = x
    l2.append(min)
    l.remove(min)
print(l)
print(l2)