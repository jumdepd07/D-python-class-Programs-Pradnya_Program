s = 'Pradnya Naresh Jumde Pune'
dict = {}
for i in s:
    if i in dict.keys():
        dict[i] = dict[i]+1
    else:
        dict[i] = 1
for k,v in dict.items():
    print(f"{k} = {v}times")
