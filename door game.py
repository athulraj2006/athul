#created by athul raj
#date:13-12-2024
# program to check our choice is correct, door game
def monty():
    from random import randint
    choice=int(input("open a door(1,2 or 3):"))
    a=randint( 1, 4)
    if a==choice:
        secondchoice=input("opens th door,revealing a car\nDo you want to switch your door(Y/N):")
        secondchoice.casefold()
        if secondchoice=='y':
            finalchoice=input("enter your final choice:")
            if finalchoice==a:
                print("congrats you won the car")
            else:
                print("congrats you won a goat")
        else:
            print("congrats you won a car")
    else:
        secondchoice=input("opens the door,revealing a goat\nDo you want to switch your door(Y/N):")
        if secondchoice=='y':
            finalchoice=input("enter your final choice:")
            if finalchoice==a:
                print("congrats you won a car")
            else:
                print("congrats you won a goat")
        else:
            print("congrats you won a GOAT")
monty()
