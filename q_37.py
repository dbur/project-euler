import math
answer_sum = 0
answer_array = set()

def is_prime(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    for i in range(2,1+math.ceil(math.sqrt(n))):
        if (n%i==0):
            return 0
    return 1

for check_truncatable_prime in range(11,1000000,2):
    sub_prime = 1
    if(is_prime(check_truncatable_prime)):
        print(str(check_truncatable_prime) + ": yes")
        for num_len in range(1,len(str(check_truncatable_prime))):
            this_num = int(str(check_truncatable_prime)[0:num_len])
            if(is_prime(this_num)):
                print(str(this_num) + ": sub-yes")
            else:
                sub_prime=0
                break
        if(not(sub_prime)):
            continue
        for num_len in range(1,len(str(check_truncatable_prime))):
            this_num = int(str(check_truncatable_prime)[num_len:len(str(check_truncatable_prime))+1])
            if(is_prime(this_num)):
                print(str(this_num) + ": sub-yes")
            else:
                sub_prime=0
                break
        if(not(sub_prime)):
            continue
        else:
            answer_array.add(check_truncatable_prime)
            answer_sum += check_truncatable_prime
        if (len(answer_array)==11):
            break

print(answer_array)
print(len(answer_array))
print(answer_sum)
