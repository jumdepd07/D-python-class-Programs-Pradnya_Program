file_name = 'Test1.txt'
f = open(file_name,'r')
data = f.read()
l1 = data.split()
for word in l1:
    if word.isupper():
        print(word)
    if word.isnumeric():
        print(word)

f.close