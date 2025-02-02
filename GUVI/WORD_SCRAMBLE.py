#Word scramble

import random
#declearing the string values
words= ("python","guvi","java","selenium","automation")
#defining the function of the scramble word
def scramble_word(word):
    scramble_word =''.join(random.sample(word,len(word)))
    return scramble_word
#condition to find the user guess the correct ans
while True:
    selected_word=random.choice(words)
    user_words=input("unscramble the word :"+scramble_word(selected_word))
    if user_words == selected_word:
        print("correct")
        break
    else :
         print("try again")
         