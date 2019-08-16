import csv
import random

with open("expenses.csv","w+",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Expenses"])
    numweeks = 30
    temprr = []
    for x in range(1,numweeks*7+1):
        dailyex = random.uniform(250,300)
        if x%7==2:
            dailyex+=50
        if x%7==4:
            dailyex+=100
        if x%7==5:
            dailyex+=25
        if x%10==0:
            dailyex+=30
        writer.writerow([dailyex])
