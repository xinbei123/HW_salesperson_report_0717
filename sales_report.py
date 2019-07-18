"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
# making a variable called salespeople as a empty list

melons_sold = []
# making a variable called melons_sold as a empty list

f = open('sales-report.txt')
# creating a variable called f(like a file) 
# using the built in function open to open a txt file and stored in f

for line in f:
# in file f, iterate over each line

    line = line.rstrip()
    # strip off whitespace after each line
    entries = line.split('|')
    # split up each line by pipe operator, returns a list of strings

    salesperson = entries[0]
    # salesperson is assigned at index 0 of each line

    melons = int(entries[2])
    # melons are assigned at index 2 (as integer)

    if salesperson in salespeople:
    # checking each salesperson in the empty salespeople list

        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold} melons')
