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

abundant_nums = []
the_answer = 1
top_range = 28124
for i in range(2,top_range):
    if is_abundant(i):
        abundant_nums.append(i)
    the_answer += i
    print(i)

remove_these = set()
for i in range(0,len(abundant_nums)):
    for j in range(i,len(abundant_nums)):
        if(abundant_nums[i]+abundant_nums[j]<top_range):
            remove_these.add(abundant_nums[i]+abundant_nums[j])
        else:
            break
        print(i,j)


print(the_answer)
print(sum(remove_these))
print(the_answer-sum(remove_these))
