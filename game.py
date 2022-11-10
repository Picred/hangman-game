import random
import string
import os
import time

def game_condition(temp_word: string, lives: int, selected_word: string) -> bool:
    
    if selected_word == temp_word:
        print(f"You won, you guessed the word {selected_word}")
        return False

    elif lives==0:
        print(f"Game over! You lost all lives. The word was {selected_word}")
        return False
        
    return True


def main(play_game: bool) -> None:

    while play_game:
        lives = 7
        alphabet = list(string.ascii_lowercase) 
        f = open('list_of_words.txt', "r") #list of all words
        words = f.readlines()

        random_word = words[random.randint(0,len(words)-1)]

        selected_word = random_word.replace("\n","") #word to guess

        shown_word = "" #the word with '?' to show progressively

        for i in selected_word:
            shown_word+='?'

        while game_condition(shown_word, lives,selected_word):

            os.system('cls')
            current_alphabet = ""
            for i in alphabet:
                current_alphabet+= i + " "

            print(f"Available letters: {current_alphabet}")

            print("\nThe word to guess is: " + shown_word + "\tLives: " + str(lives) + "")

            input_choice = input("Choose a letter: ")

            try: #try to remove a letter from the alphabet
                alphabet.remove(input_choice)
            except:
                print("Not available letter!")
                time.sleep(1)
                continue

            #update shown word, remove some '?', if needed, and replace them with input_choice
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
            if(input("\nPress 'q' + 'ENTER' to quit the game: ") == 'q'):
                play_game=False

    f.close()

if __name__ == "__main__":
    main(play_game = True)
