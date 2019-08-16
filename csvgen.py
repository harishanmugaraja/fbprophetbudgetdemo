#Hari Shanmugaraja      08/16/19
import csv
import random
import datetime

with open("expenses.csv","w+",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ds","y"])
    numweeks = 30
    temprr = []
    date = datetime.datetime(2019,8,19)
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
        writer.writerow([date,dailyex])
        date += datetime.timedelta(days=1)
