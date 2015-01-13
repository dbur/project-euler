answers = []
for i in range(2,1000000):
    the_sum=0
    for j in range(0,len(str(i))):
        the_sum += (int(str(i)[j])**5)
    if the_sum==i:
        print(the_sum)
        answers.append(i)
print(answers)
print(sum(answers))