answer = []

def fact(i):
    if (i == 1 or i==0):
        return 1
    else:
        return i*fact(i-1)

looking_for_answer = 1
i=40586
while looking_for_answer:
    sum=0
    for j in range(0,len(str(i))):
        sum += fact(int(str(i)[j]))
    print (i,sum)
    looking_for_answer = not (i==sum)
    i += 1

# 145, 40585

# not sure how to find the upper limit of the loop...but the sum of those two produced the answer.