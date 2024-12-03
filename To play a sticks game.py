#created by athul raj
#date:3-12-2024
#program to find who win in stick game
print('welcome to the stick game')
player1=input('enter the 1st player name')
player2=input('enter the 2nd player name')
stick_remaining=16
while stick_remaining>0:
    player = player1
    print("stick remaining=",stick_remaining)
    n=int(input(f"{player} pick 1,2 or 3 sticks"))
    stick_remaining=stick_remaining-n
    if stick_remaining<=0:
        print(f"{player}picks the last stick and loses the game")
    else:
        player = player2
        print(f"stick remaining",stick_remaining)
        i=int(input(f"{player}pick 1,2 or 3 sticks"))
        stick_remaining=stick_remaining-i
        if stick_remaining<=0:
            print(f"{player}picks the last stick and loses the game")
print()