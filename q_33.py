answer = []

for numerator in range(10,100):
    numerator_first_digit = str(numerator)[0]
    numerator_second_digit = str(numerator)[1]
    for denominator in range(int(numerator_first_digit)*10,(int(numerator_first_digit)+1)*10):
        if denominator<10 or numerator==denominator:
            break
        denominator_second_digit = str(denominator)[1]
        if int(denominator_second_digit) == 0:
            continue
        if numerator / denominator == int(numerator_second_digit) / int(denominator_second_digit):
            answer.append([numerator,denominator])
    for denominator in range(int(numerator_second_digit)*10,(int(numerator_second_digit)+1)*10):
        if denominator<10 or numerator==denominator:
            break
        denominator_second_digit = str(denominator)[1]
        if int(denominator_second_digit) == 0:
            continue
        if numerator / denominator == int(numerator_first_digit) / int(denominator_second_digit):
            answer.append([numerator,denominator])

print(answer)
numerator=1
denominator=1
for x in answer:
    numerator *= x[0]
    denominator *= x[1]
print (numerator,denominator)

while 1:
    reduced = 0
    for i in range(2,min(int(numerator),int(denominator))+1):
        if numerator%i==0 and denominator%i==0:
            numerator /= i
            denominator /= i
            reduced=1
    if not reduced:
        break

print (numerator,denominator)