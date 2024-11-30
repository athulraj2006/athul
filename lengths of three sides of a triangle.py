#created by athul raj
#date:30-11-2024
def righttrianglecheck():
    a=int(input("enter first side:"))
    b=int(input("enter second side:"))
    c=int(input("enter third side:"))
    list1=[a,b,c]
    list1.sort()
    if list1[2]**2==list1[0]**2+list1[1]**2:
        print("It is a rirht triangle")
    else:
        print("It is not a right triangle")
righttrianglecheck()

