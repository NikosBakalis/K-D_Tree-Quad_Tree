import random
import decimal

points = []
file = open("test.txt","w")

for i in range(0,2000):
    x = float(decimal.Decimal(random.randrange(-10000, 10000)) /10)
    y = float(decimal.Decimal(random.randrange(-10000, 10000)) /10)
    file.write(str((x,y)) + "\n")

file.close()