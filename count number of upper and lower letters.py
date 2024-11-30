#created by athul raj
#date:30-11-2024
def upperlower():
    string1=input("enter a string")
    uppercount=0
    lowercount=0
    for i in string1:
     if i.isupper():
        uppercount+=1
     elif i.islower():
        lowercount+=1
    print("no. of upper case characters",uppercount)
    print("no. of lower case characters",lowercount)
upperlower()