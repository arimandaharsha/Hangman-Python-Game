import random
import resources
chosen_word = resources.word_list[random.randint(0,len(resources.word_list))]
game_over = False
lives = 6

print(resources.logo,"\n"*2)
cwlist = []
guess_letters = []
for i in range(len(chosen_word)):
    cwlist.append("_")

print(cwlist)
while not game_over:
    print("Lives Remaining : ", lives)
    guess = input("enter a letter").lower()

    if guess in guess_letters:
        print("You already entered the letter ",guess)
        continue
    guess_letters.append(guess)

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            cwlist[i] = guess
    if guess not in chosen_word:
        lives = lives-1
        print(guess," is not present in the word")

        if lives == 0:
            print(resources.stages[lives])
            print(f"YOU LOSE :(\nWord is {chosen_word}")
            break


    if "_" not in cwlist:
        game_over = True
        print(cwlist)
        print("YOU WON!!!")
        break
    print(resources.stages[lives])
    print(cwlist)

