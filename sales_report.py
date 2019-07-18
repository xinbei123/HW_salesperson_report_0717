"""Generate sales report showing total melons each salesperson sold."""

# create a variable called salespeople as a empty list
salespeople = []

# create a variable called melons_sold as a empty list
melons_sold = []

# creating a variable called f(like a file) 
# using the built in function open to open a txt file and stored in f
f = open('sales-report.txt')

# in file f, iterate over each line
for line in f:

    # strip off whitespace after each line
    line = line.rstrip()

    # split up each line by pipe operator, returns a list of strings
    entries = line.split('|')
    
    # salesperson is at index 0 of each line
    salesperson = entries[0]
    
    # melons are at index 2 (as integer)
    melons = int(entries[2])
    
    # if salesperson already in the salespeople list
    # the melon_sold total will be added at that index
    # if salesperson is not in the salespeople list
    # salesperson and melon_sold will be added to the empty list salespeople
    if salesperson in salespeople:

        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# iterate over salespeople list, print number of melons each salesperson sold                
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold} melons')
