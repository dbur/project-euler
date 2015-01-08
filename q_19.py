days_in_month = [31]*13
days_in_month[9]=days_in_month[4]=days_in_month[6]=days_in_month[11]= 30
days_in_month[2]= 28
print(days_in_month)
current_date = [1900,1,1,1]
sundays_on_first = 0
while current_date[0]<2001:
    print(current_date)
    if current_date[2] == 1 and current_date[3] == 7 and current_date[0]>=1901 and current_date[0]<=2000: # 7 is sunday
        sundays_on_first += 1
        print("DING")

    current_date[3] = current_date[3] % 7 + 1 # add day
    if (current_date[0]%100!=0 or current_date[0]%400==0) and current_date[0]%4==0 and current_date[1]==2 and current_date[2]==28:
        current_date[2] = 0 # if leap year (set to 0 instead of 29 for %)
    else:
        current_date[2] = current_date[2] % days_in_month[current_date[1]] + 1
        if current_date[2] == 1:
            current_date[1] = current_date[1] % 12 + 1
            if current_date[1] == 1:
                current_date[0] += 1

print(sundays_on_first)
