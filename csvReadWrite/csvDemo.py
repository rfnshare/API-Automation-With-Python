import csv

with open('../utilities/loanapp.csv', 'r') as csvFile:
    data = csv.reader(csvFile, delimiter=',')
    # print(data)
    # print(list(data))
    names = []
    status = []
    for i in data:
        names.append(i[0])
        status.append(i[1])
print(names)
print(status)
