def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

val = str(fact(100))
sum=0
for i in range(0,len(val)):
    sum+= int(val[i])
print(sum)
