import csv
import random

columns = 100
rows = 100

with open("F:\simpleDataSet.csv", "a", newline='') as f:
    writer = csv.writer(f)
    for k in range(rows):
        row = []
        for i in range(columns):
            row.append(random.uniform(100, 500))
        writer.writerow(row)
