import math

for decimal_number in range(1,1000000):
    if str(decimal_number) == str(decimal_number)[::-1]:
        print(str(decimal_number)+" : true"