import sys
import csv


with open(f"{sys.argv[1]}") as file:
    reader = csv.reader(file)

    for row in reader:
        r = []
        for column in row:
            r.append(column)
        