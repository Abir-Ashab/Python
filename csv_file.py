import csv
# default newline add hobe
with open('data.csv', 'w', newline= '') as output : 
    # writing file
    output_file = csv.writer(output)
    output_file.writerow(["niloy", '1315', 'comilla'])
    output_file.writerow(["abir", '1315', 'comilla'])
    output_file.writerow(["ashab", '1315', 'comilla'])

output.close()

# newline hishebe just last e ekta space add hobena
# output = open('data.csv', 'w')


# reading file
input = open('data.csv', 'r')
input_file = csv.reader(input)
# print(input_file)
data = list(input_file)
print('data are ', data)
for i in range(0, len(data)) :
    print(data[i], ' ')