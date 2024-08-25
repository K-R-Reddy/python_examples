import random
def choose():
    words=['rainbow','computer','science','python','java','cobra','spyder','anaconda','water','tree']
    pickword=random.choice(words)
    return pickword
def jumble(word):
   jumbledword="".join(random.sample(word,len(word)))
   return jumbledword
def thank(player1,player2,p1,p2):
    print(player1," your score is",p1)
    print(player2," your score is",p2)
    if p1>p2:
        print("Congrulations",player1,"! you win the Game")
    else:
        print("Congrulations",player2,"! you win the Game")
def play():
    player1=input("Enter Player1 Name : ")
    player2=input("Enter Player2 Name : ")
    p1=0
    p2=0
    turn=0
    while(1):
        #Computers task
        pick=choose()
        qn=jumble(pick)
        print(qn)
        if turn%2==0:
            print(player1,"Turn : ")
            ans=input("What is on my mind? ")
            if ans==pick:
                p1+=1
                print(player1," Score is ",p1)
            else:
                print("Better Luck Next Time I Thought :",pick)
            c=int(input("press 1 to Continue : "))
            if c!=1:
                thank(player1,player2,p1,p2)
                break
        #player2
        else:
            print(player2,"Turn : ")
            ans=input("What is on my mind? ")
            if ans==pick:
                p2+=1
                print(player2," Score is ",p1)
            else:
                print("Better Luck Next Time I Thought :",pick)
            c=int(input("press 1 to Continue : "))
            if c!=1:
                thank(player1,player2,p1,p2)
                break
        turn+=1
play()