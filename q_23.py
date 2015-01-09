import math

def is_abundant(the_num):
    the_sum=1
    for i in range(math.floor(math.sqrt(the_num)),1,-1):
        if the_num%i==0:
            if i == the_num/i:
                the_sum+=i
            else:
                the_sum+=i+(the_num/i)
            if the_sum>the_num:
                return 1
    return 0

sum_of_abundant_nums = []
abundant_nums = []
the_answer = 1
next_sum_to_check=0
for i in range(2,28125):
    if is_abundant(i):
        abundant_nums.append(i)
        for a in range(0,len(abundant_nums)):
            sum_of_abundant_nums.append(i+abundant_nums[a])
        sum_of_abundant_nums = sorted(sum_of_abundant_nums)
    if abundant_nums == []:
        the_answer += i
        continue
    if i == sum_of_abundant_nums[next_sum_to_check]:
        while i==sum_of_abundant_nums[next_sum_to_check]:
            next_sum_to_check+=1
        continue
    the_answer += i
    print(i)

print(the_answer)
print(abundant_nums[0:10])


