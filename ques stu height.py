#created by athul raj
#date:15-08-24
num=int(input("enter number of students in a class: "))
b_total=0
tbh=0
g_total=0
tgh=0
for i in range(0,num):
    gender=input("enter gender")
    height=int(input("enter height"))
    if gender=="m":
        b_total+=1
        tbh=tbh+height
    else:
        g_total+=1
        tgh=tgh+height
avg_bh=tbh/b_total
print(avg_bh)
avg_gh=tgh/g_total
print(avg_gh)





