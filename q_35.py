import math
def check_prime(the_num):
    for x in range(2,math.ceil(math.sqrt(the_num))+1):
        if the_num % x == 0:
            return 0
    return 1

i=3
count_circ=1 # 2 works...
while i <= 1000000:
    is_circular_prime = 1
    for j in range(0,len(str(i))):
        to_check = int(str(i)[j:len(str(i))]+str(i)[0:j])
        if not check_prime(to_check):
            is_circular_prime = 0
            break
    if is_circular_prime:
        count_circ +=1
        print(i)
    i+=2
    for j in range(0,len(str(i))):
        if int(str(i)[j]) % 2 ==0:
            i = int(str(i)[:j]+str(int(str(i)[j])+1)+str(i)[j+1:])

print (count_circ)