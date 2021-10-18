with open("seznam.csv", "r") as seznam:
    seznam_rows = seznam.read().splitlines()

for row in seznam_rows:
    row_data = row.split(",")
    if len(row_data) == 3:
        print("{0} is {1} years old and {2}.".format(row_data[0],row_data[1],row_data[2]))