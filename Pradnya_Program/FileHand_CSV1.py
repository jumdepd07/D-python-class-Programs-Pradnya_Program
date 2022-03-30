import csv
file_name = r'D:\\python class\\Students_data_batch_4.csv'
f = open(file_name, 'r')

data = list(csv.reader(f))

for row in data:
    print(row,'\t')
f.close