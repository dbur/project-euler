a_val=200
b_val=100
c_val=50
d_val=20
e_val=10
f_val=5
g_val=2
h_val=1

vals=[a_val,b_val,c_val,d_val,e_val,f_val,g_val,h_val]


answer=0
this_combo=[0]*6
temp_sum=0
the_goal=200
for a in range(0,int(the_goal/a_val)+1):
    for b in range(0,int(the_goal/b_val)+1):
        if (b*b_val+a*a_val>the_goal):
            break
        for c in range(0,int(the_goal/c_val)+1):
            if (c*c_val+b*b_val+a*a_val>the_goal):
                break
            for d in range(0,int(the_goal/d_val)+1):
                if (d*d_val+c*c_val+b*b_val+a*a_val>the_goal):
                    break
                for e in range(0,int(the_goal/e_val)+1):
                    if (e*e_val+d*d_val+c*c_val+b*b_val+a*a_val>the_goal):
                        break
                    for f in range(0,int(the_goal/f_val)+1):
                        if (f*f_val+e*e_val+d*d_val+c*c_val+b*b_val+a*a_val>the_goal):
                            break
                        for g in range(0,int(the_goal/g_val)+1):
                            if (g*g_val+f*f_val+e*e_val+d*d_val+c*c_val+b*b_val+a*a_val>the_goal):
                                break
                            for h in range(0,int(the_goal/h_val)+1):
                                if (h*h_val+g*g_val+f*f_val+e*e_val+d*d_val+c*c_val+b*b_val+a*a_val>the_goal):
                                    break
                                elif h*h_val+g*g_val+f*f_val+e*e_val+d*d_val+c*c_val+b*b_val+a*a_val == the_goal:
                                    print(a,b,c,d,e,f,g,h)
                                    answer+=1
print(answer)

