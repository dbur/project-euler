answer = []
# a * b = c
# digitwise a+b+c=9
# a<b<c
# 2,3,4
# 1,4,5
# 1,3,6

# range digits (a) = 1-2
for multiplicand in range(1,100):
    digits = len(str(multiplicand))
    # range digits (b) = 2-3
    for multiplier in range(100,10000):
        all_digits = list(str(multiplier)+str(multiplicand)+str(multiplicand*multiplier))
        if len(all_digits)>9:
            continue
        if len(set(all_digits)) == 9 and '0' not in set(all_digits):
            print(sorted(set(all_digits)),multiplicand,multiplier,multiplier*multiplicand)
            answer.append(multiplier*multiplicand)

print(sum(set(answer)))