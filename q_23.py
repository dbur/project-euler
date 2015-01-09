def is_abundant(the_num):
    the_sum=0
    for i in range(the_num-1,1,-1):
        if the_num%i==0:
            the_sum+=i
            if the_sum>the_num:
                return 1
    return 0

sum_of_abundant_nums = []
abundant_nums = []
the_answer = 0
for i in range(1,28123+1):
    if is_abundant(i):
        abundant_nums.append(i)
        for z in abundant_nums:
            sum_of_abundant_nums.append(z+i)
    if i in sum_of_abundant_nums:
        continue
    the_answer += i
    print(i)

print(the_answer)