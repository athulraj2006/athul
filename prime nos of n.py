number=int(input("enter a number:"))
isPrime = True
for i in range(2,number//2+1):
    if number % i ==0:
        isPrime = False
        break
if isPrime:
    print(f"the given number {number} is prime")
else:
    print(f"the given number {number} is not prime")