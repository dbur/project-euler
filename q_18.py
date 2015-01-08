given = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
given=str.split(given,'\n')
given = [i.split(' ') for i in given]
given = [[int(y) for y in x] for x in given]


def check_path_validity(the_path):
    for x in range(0,len(the_path)-1):
        if(the_path[x]!=the_path[x+1] and the_path[x+1]!=the_path[x]+1):
            return 0
    return 1

def next_best_path(the_path,the_triangle):
    next_best_path = list(the_path)
    diff = list(the_path)
    for i in range(0,len(the_triangle)):
        current_max_val = the_triangle[i][the_path[i]]
        next_max_val = -1
        for end_part in range(the_path[i]+1,len(the_triangle[i])):
            if the_triangle[i][end_part] == current_max_val:
                next_best_path[i] = end_part
                break
            elif the_triangle[i][end_part] < current_max_val and the_triangle[i][end_part] > next_max_val:
                next_best_path[i] = end_part
                next_max_val = the_triangle[i][end_part]
        for start_part in range(0,the_path[i]):
            if the_triangle[i][start_part] < current_max_val and the_triangle[i][start_part] >= next_max_val:
                next_best_path[i] = start_part
                next_max_val = the_triangle[i][start_part]
        diff[i] = the_triangle[i][the_path[i]] - the_triangle[i][next_best_path[i]]
    lowest_val = max(diff)
    change_this=-1
    to_this=-1
    for x in range(0,len(diff)):
        if(the_path[x]!=next_best_path[x] and diff[x]<lowest_val):
            change_this = x
            to_this = next_best_path[x]
            lowest_val = diff[x]
    next_best_path = list(the_path)
    next_best_path[change_this] = to_this
    return next_best_path

path_to_take = []

for i in range(0,len(given)):
    for j in range(0,len(given[i])):
        if (max(given[i])==given[i][j]):
            path_to_take.append(j)
            break
need_valid_path=not(check_path_validity(path_to_take))

while need_valid_path:
    path_to_take = next_best_path(path_to_take,given)
    need_valid_path = not(check_path_validity(path_to_take))
    print(path_to_take)
    
  

print (path_to_take)

