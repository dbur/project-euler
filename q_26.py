from decimal import * 
import math
getcontext().prec=100

longest_answer=[0,0]
for i in range(1,1000):
    answer = 0
    answer_repeat = []
    remainder = [(10 % i )*(10**len(str(i)))]
    repeat=0
    while 1:
        latest = remainder[len(remainder)-1]
        if latest == 0:
            break
        to_add = (latest %(math.floor(latest/i)*i))*(10**len(str(i)))
        remainder.append(to_add) 
        if to_add in remainder[0:len(remainder)-1]:
            repeat=1
            break
    if repeat:
        for j,val in enumerate(remainder):
            if (val == remainder[len(remainder)-1]):
                answer_repeat = remainder[j:len(remainder)-1]
                longest_answer = [i,len(answer_repeat)] if len(answer_repeat) > longest_answer[1] else longest_answer
                break

print(longest_answer)