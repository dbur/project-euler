from decimal import * 
import math
getcontext().prec=100

num = 0
for i in range(1,11):
    remainder = [(10 % i )*10]
    while 1:
        latest = remainder[len(remainder)-1]*10
        if latest == 0:
            break
        to_add = (latest % math.floor(latest/i))*10
        remainder.append(to_add) 
        if to_add in remainder[0:len(remainder)-1]:
            break
    print(i,remainder,1/i)