check_prime=int(input("enter a number"))
for i in range(2,(check_prime//2)+1):
    if check_prime % i==0:
        break
    if i==(check_prime//2):
        print(f"{check_prime} is a prime number")
    else:
        print(f"{check_prime} ssis not a prime number")
