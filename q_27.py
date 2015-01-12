import math

def is_prime(a):
    if a <=1:
        return 0
    for i in range (2,math.ceil(math.sqrt(a))):
        if a%i==0:
            return 0
    return 1


max_consecutive = ['i','j',0]
min_range = -999
max_range = 1000
for i in range(min_range,max_range):
    for j in range(min_range,max_range):
        consecutive = 0
        while 1:
            check_val=consecutive**2+i*consecutive+j
            if is_prime(check_val):
                consecutive +=1
            else:
                break
        max_consecutive = (i,j,consecutive) if consecutive > max_consecutive[2] else max_consecutive

print("max_consecutive",max_consecutive[0]*max_consecutive[1],max_consecutive)