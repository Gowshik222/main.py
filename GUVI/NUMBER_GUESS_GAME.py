#Number gussing game
import random
#declearing the values
numbers=random.randint(1,30)
score=0
#condition to guess the user is correct
while True:
    user_num=int(input())

    if user_num<numbers:
        print("too low,try again")
    elif user_num>numbers:
          print("too high,try again")
    else :
          print("correct")
          score +=1
          print(score)    
          break