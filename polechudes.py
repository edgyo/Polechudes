from random import randint
from os import system, name 
from time import sleep 
import os, sys, time

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

wordlist = []
game_version = ''

game_version_file = 'game_version.txt'
animals_list_file = 'animals.txt'
clothes_list_file = 'clothes.txt'
fruit_list_file = 'fruit.txt'
furniture_list_file = 'furniture.txt'
pirates_list_file = 'pirates.txt'

with open(game_version_file, 'r') as file: # importing version from txt file
    game_version = file.read() 

def wordlist_preparation(): # importing text files with game words and returning the list for current game
    with open(animals_list_file, 'r') as file:
        animals_list = file.read().split()
    with open(clothes_list_file, 'r') as file:
        clothes_list = file.read().split()
    with open(fruit_list_file, 'r') as file:
        fruit_list = file.read().split()
    with open(furniture_list_file, 'r') as file:
        furniture_list = file.read().split()
    with open(pirates_list_file, 'r') as file:
        pirates_list = file.read().split()
    words_list = [animals_list, clothes_list, fruit_list, furniture_list, pirates_list]
    return words_list

def word_random (wordlist): # picking and returning a random word and theme to play
    whole_list = wordlist
    random_list_index = randint(1,len(whole_list)-1)
    theme_list = whole_list[random_list_index]
    random_word_index = randint(1,len(theme_list)-1)
    rand_word = theme_list[random_word_index].lower()

    while (len(rand_word) < 3):
        random_word_index = randint(1,len(theme_list)-1)
        rand_word = theme_list[random_word_index].lower()

    if (random_list_index == 0):
        game_theme = 'animals'
    if (random_list_index == 1):
        game_theme = 'clothes'
    if (random_list_index == 2):
        game_theme = 'fruit'
    if (random_list_index == 2):
        game_theme = 'furniture'
    if (random_list_index == 2):
        game_theme = 'pirates'

    return [rand_word, game_theme]

def word_guessing (word, game_theme): # game script
    score = 0
    word_hidden = '*' * len(word)

    for i in range(len(word)): # showing space and dash characters if any appear
        if (word[i] == '-'):
            word_hidden = word_hidden[:i] + '-' + word_hidden[i+1:]
        if (word[i] == ' '):
            word_hidden = word_hidden[:i] + ' ' + word_hidden[i+1:]

    letters_guessed = [] # list with letters already guessed
    print(100*"\n")
    print('The theme is {}. Your word currently is {}!'.format(game_theme, word_hidden))

    while (word_hidden.find('*') >= 0): # game runs until all the characters are revealed
        print("\nTell me a letter!\n")
        letter_input = input()
        clear()
        print(100*"\n")
        if (word.find(letter_input) >= 0) and (letter_input not in letters_guessed):
            for i in range(len(word)):
                if (word[i] == letter_input):
                    word_hidden = word_hidden[:i] + letter_input + word_hidden[i+1:]
                    score += 200        
            print("You guessed the letter! Your score is now {} points.".format(score))
        else:
            score -= 100
            print("I'm sorry but there's no such a letter.")
            print("Your score has been decreased by 100 and is {} points now.".format(score))

        letters_guessed.append(letter_input)
        print("Theme: {}. Your word currently is {}.".format(game_theme, word_hidden))
    print(100*"\n")
    print("Congradulations! You guessed the word - {}. Your score is {}!".format(word, score))

def main(): # main starting function
    print("Welcome to Polechudes {}!\n".format(game_version))
    #print("Welcome to Polechudes!\n")
    while(True):
        print("Are you ready to play? (y/n)")
        player_answer = input()
        if (player_answer == 'y'):
            [word, theme] = word_random(wordlist_preparation())
            word_guessing(word, theme)
        else:
            print("Thanks for playing!")
            time.sleep(3)
            break

main()