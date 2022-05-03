import random 

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp =='R':
        if you=='S':
            return False
        elif you=='P':
            return True
    elif comp =='P':
        if you=='R':
            return False
        elif you=='S':
            return True
    elif comp =='S':
        if you=='P':
            return False
        elif you=='R':
            return True

print("comp Turn: Rock(R) Paper(P) or (S)scissor")
randNo = random.randint(1,3)
if randNo ==1:
    comp = 'R'
elif randNo == 2:
    comp = 'P'
elif randNo == 3:
    comp = 'S'


you = input("Yours Turn: Rock(R) Paper(P) or (S)scissor")
a = gameWin(comp, you)

print(f"Computer chose{comp}")
print(f"You choose {you}")
if a ==None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You Lose!")




