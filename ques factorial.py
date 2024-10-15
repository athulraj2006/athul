#created by athul raj
#date:15-10-24
num=int(input("enter number of which factorial is wanted;"))
fact=1
if num<0:
    print("enter positive number")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range (1,num+1):
      fact=fact*i
print("factorial of number is:,",fact)


