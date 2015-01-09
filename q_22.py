def score_name(the_name):
    score = 0
    for i in range(0,len(the_name)):
        score += ord(the_name[i])-96
    print(the_name)
    print(score)
    return score

names_file = open('p022_names.txt')
names_rank = sorted(str.split(str.replace(names_file.readline().lower(),"\"",""),","))
answer = 0
for a,b in enumerate(names_rank):
    answer += (a+1)*score_name(b)

print (answer)
