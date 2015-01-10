digits = [0,1,2,3,4,5,6,7,8,9]

def next_value(given,index):
    current_value = given[index]
    local_min = max(given)+1
    local_min_index = index
    
    for i in range(index+1,len(given)):
        val = given[i]
        if val < local_min and val > current_value:
            local_min = val
            local_min_index = i
    if local_min_index != index:
        given[index] = local_min
        given[local_min_index] = current_value
        given = given[0:index+1] + sorted(given[index+1:len(given)])
    elif index>0:
        given = next_value(given,index-1)
    return given
    
print(digits)

for i in range(999999):
    digits = next_value(digits,len(digits)-1)


print(digits)