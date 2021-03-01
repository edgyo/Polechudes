from random import randint
wordlist = []
version = open('version.txt', 'r').read() # importing version from txt file

def wordlist_preparation(): # importing text files with game words and returning the list for current game
    animals_list = []
    clothes_list = []
    fruit_list = []
    with open('animals.txt', 'r') as file:
        animals_list = file.read().split()
    with open('clothes.txt', 'r') as file:
        clothes_list = file.read().split()
    with open('fruit.txt', 'r') as file:
        fruit_list = file.read().split()
    words_list = [animals_list, clothes_list, fruit_list]
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
        print("Your word currently is {}.".format(word_hidden))
    print(100*"\n")
    print("Congradulations! You guessed the word - {}. Your score is {}!".format(word, score))

def main(): # main starting function
    print("Welcome to Polechudes {}!\n".format(version))
    while(True):
        print("Are you ready to play? (y/n)")
        player_answer = input()
        if (player_answer == 'y'):
            [word, theme] = word_random(wordlist_preparation())
            word_guessing(word, theme)
        else:
            print("Thanks for playing!")
            break

main()