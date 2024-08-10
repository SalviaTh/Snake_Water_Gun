import random
'''
1 for snake
-1 for Water
0 for Gun
'''
print("Welcome!Let's play Snake Water Gun Game")
point=int(input("Enter Winning Point: "))
computerpt=0
youpt=0
while True:
    r=[1,-1,0]
    Computer=random.choice(r)

    youstr =input("Enter your choice s/w/g:")
    youdic={
        "s":1,"w":-1,"g":0
    }
    if youstr not in youdic:
        print("Invalid Input!!!")
        continue
    reversedict={
        1:"Snake",-1:"Water",0:"Gun"
    }

    younum =youdic[youstr]
    print(f"you choose {reversedict[younum]}\nComputer choose {reversedict[Computer]}")
    if((Computer==-1 and younum==1)or(Computer==1 and younum==0)or(Computer==0 and younum==-1)):
        print("You Win!")
        youpt+=1
    elif((Computer==-1 and younum==0)or(Computer==0 and younum==1)or(Computer==1 and younum==-1)):
        print("You lose!")
        computerpt+=1
    elif(Computer==younum):
        print("Draw")
    else:
        print("Something Went Wrong")
    if youpt==point or computerpt==point:
        break

print("Game over")
if(youpt==point):
    print(f"You Win the Game with points {youpt} and {computerpt}")
else:
    print(f"You lose the Game {youpt} snd {computerpt} ")