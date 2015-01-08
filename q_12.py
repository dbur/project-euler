import math
triangle_number_value=0
triangle_number_rank=0
num_divisors=0

while num_divisors < 500:
    triangle_number_rank+=1
    triangle_number_value+=triangle_number_rank
    num_divisors=2
    for i in range(2,math.floor(math.sqrt(triangle_number_value))):
        if(triangle_number_value%i==0):
            num_divisors+=2
    print(str(triangle_number_rank)+" "+str(triangle_number_value)+" "+str(num_divisors))
