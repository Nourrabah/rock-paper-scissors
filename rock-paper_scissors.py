score1=0
score2=0
rock="rock"
papier="papier"
scissors="scissors"
parts=int(input("how many parts do wanna play? "))
while(parts<=0):
    print("u need at least one round")
    parts=int(input("how many rounds do wanna play? "))
    
for i in range(1,parts+1):
    print("round number: ",i)
    player1=input("player 1 choose: ")
    player2=input("player 2 choose: ")
    
        
    if(player1==scissors and player2==rock):
        print("player2 won ")
        score2+=1
        
    elif(player1==papier and player2==rock):
        print("player 1 won")
        score1+=1
        
    elif(player1==scissors and player2==papier):
        print("player 1 won ")
        score1+=1
        
    elif(player1==player2):
        print("its a dom")
    else :
    
        print("player 2 won")
        score2+=1
            
print("end of the game good job hers your scores: player1:",score1,"player2:",score2)