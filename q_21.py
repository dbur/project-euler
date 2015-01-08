def find_d(a):
    d_sum = 0
    for i in range(1,a):
        if a%i ==0:
            d_sum+=i
    return d_sum
answer=set()
for a in range(1,10000):
    if a in answer:
        continue
    b = find_d(a)
    if (a == find_d(b) and a!=b):
        answer.add(a)
        answer.add(b)
    print(a,b)
print(sum(answer))