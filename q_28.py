
square_side = 1001
sum = 1
cur_val=1
for square in range(3,square_side+1,2):
    for i in range(4):
        cur_val += (square-1)
        sum += cur_val
print(sum)
