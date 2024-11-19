#created by athulraj
#date:19-11-24
list1=[]
limit=int(input('enter number of elements to be put in list:'))
for i in range(limit):
    num=int(input("enter the even element:"))
    list1.append(num)

list2=[]
limit=int(input('enter number of elements to be put in list:'))
for i in range(limit):
    num=int(input("enter the odd element:"))
    list2.append(num)

evenlist=[]
oddlist=[]

newlist=(list1+list2)
for i in newlist:
    if i%2==0:
        evenlist.append(i)
        evenlist.sort()
    else:
        oddlist.append(i)
        oddlist.sort()
mergedlist=evenlist+oddlist
print(mergedlist)

#for no duplication
unique_list=[]
for i in mergedlist:
    if i not in unique_list:
        unique_list.append(i)
print("orginal list is:",mergedlist)
print("the new list is:", unique_list)