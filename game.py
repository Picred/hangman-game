import random
import string

def game_condition(temp_word: string, lives: int) -> bool:
    if selected_word == temp_word:
        print("You won, you guessed the word!")
        return False
    elif lives==0:
        print("Game over! You lost all lives!")
        return False
    return True

play_game = True

while play_game:
    lives = 7
    alphabet = list(string.ascii_lowercase) 
    f = open('list_of_words.txt', "r") #list of all words
    words = f.readlines()


    _selected_word = words[random.randint(0,len(words)-1)]

    selected_word=_selected_word.replace("\n","") #word to guess

    shown_word = ""

    for i in selected_word:
        shown_word+='?'

    while game_condition(shown_word, lives):
        
        current_alphabet = ""
        for i in alphabet:
            current_alphabet+= i + " "

        print("Here are your available letters: " + current_alphabet)
        # print(current_alphabet)

        print("\n" + selected_word) #debug
        print("\nThe word to guess is: " + shown_word + "\tRemaining lives: " + str(lives) + "")

        input_choice = input("Choose a letter: ")
        
        
        print("------------------------------------------------")

        try:
            alphabet.remove(input_choice)
        except:
            print("Not available letter!")
            continue

        indexs_of_letters = []
        if input_choice in selected_word:
            for letter in range(len(selected_word)):
                if selected_word[letter] == input_choice:
                    indexs_of_letters.append(letter)
            for index in indexs_of_letters:
                shown_word = shown_word[:index] + input_choice + shown_word[index+1:]
        else: 
            lives-=1
    else:
        if(input("\nPlay again? [y/n]: ") == 'n'):
            play_game=False

#Delete used words in list_of_words
#Guess the word with an entire input word
#Hangman art