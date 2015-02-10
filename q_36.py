answer_sum = 0

def ten_to_two(n):
    max_position = 0
    binary_number = ""
    remaining_number = n
    while 2**(max_position+1) <= n:
        max_position +=1
    while max_position >=0:
        if 2**(max_position)<=remaining_number:
            remaining_number -= 2**(max_position)
            binary_number += "1"
        else:
            binary_number += "0"
        max_position -=1
    return binary_number

for decimal_number in range(1,1000000):
    if str(decimal_number) == str(decimal_number)[::-1]:
        binary_number = ten_to_two(decimal_number)
        if binary_number == binary_number[::-1]:
            print(str(decimal_number)+" : true : " + binary_number)
            answer_sum += decimal_number
print(answer_sum)
