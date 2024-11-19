#created by athulraj
#date:19-11-24
#to print different types of patterns
print("\nincreasing triangle")
row=int(input("enter the number of rows:"))
for i in range(row+1):
    for j in range(i):
        print("*",end=" ")
    print()

print("\ndecreasing triangle")
row=int(input("enter the number of rows:"))
for i in range(row,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("\nhill pattern")
row=int(input("enter the number of rows:"))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

print("\nreverse hill pattern")
row=int(input("enter the number of rows:"))
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()


