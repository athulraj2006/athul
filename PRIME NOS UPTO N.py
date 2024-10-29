#created by athul raj
#date:29-10-24
limit=int(input('enter limit:'))
for num in range(2,limit+1):
    isprime=True
    for i in range(2,(num//2)+1):
        if num % i ==0:
            isprime=False
            break
    if isprime:
        print(num)
