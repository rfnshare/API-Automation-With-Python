import csv

field_names = ['Name', 'Status']
# Read Data From CSV File
with open('../utilities/loanapp.csv', 'r') as csvFile:
    data = csv.reader(csvFile, delimiter=',')
    # print(data)
    # print(list(data))
    names = []
    status = []
    for i in data:
        names.append(i[0])
        status.append(i[1])
# print(names)
# print(status)
dic = dict(zip(names, status))
for x, y in dic.items():
    print(x, y)

indx = names.index('sam')
lnstatus = status[indx]
print("sam loan status is", lnstatus)

# Write Data To CSV File
row = ["Testing", "Approved"]
# with open('../utilities/loanapp.csv', 'a') as wFile:
#     write = csv.writer(wFile).writerow(row)