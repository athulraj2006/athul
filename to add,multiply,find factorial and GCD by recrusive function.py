#created by athul raj
#date:3-12-2024
#program to add two positive numbers using recrusive function
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
def add_numbers(n1,n2):
    if n2==0:
        return (n1)
    else:
        return add_numbers(n1+1,n2-1)
a=add_numbers(n1,n2)
print(a)

#program to multiply two positive numbers using recrusive function
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
def product_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1 + product_numbers(n1, n2 - 1)
product_numbers(n1,n2)
print(product_numbers(n1,n2))

#program to find factorial of a number
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
n=int(input("Enter a number:"))
factorial(n)

#program to find gcd of two numbers
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
g=gcd(n1,n2)
print(g)