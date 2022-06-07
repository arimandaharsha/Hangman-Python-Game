import random
import resources
chosen_word = resources.word_list[random.randint(0,len(resources.word_list))]
game_over = False
lives = 6

print(resources.logo,"\n"*2)
cwlist = []
for i in range(len(chosen_word)):
    cwlist.append("_")

print(cwlist)
while not game_over:
    print("Lives Remaining : ", lives)
    guess = input("enter a letter").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            cwlist[i] = guess
    if guess not in chosen_word:
        lives = lives-1

        if lives == 0:
            print(resources.stages[lives])
            print(f"YOU LOSE :(\nWord is {chosen_word}")
            break


    if "_" not in cwlist:
        game_over = True
        print("YOU WON!!!")
    print(resources.stages[lives])
    print(cwlist)

