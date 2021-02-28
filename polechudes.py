from random import randint
wordlist = []
version = open('version.txt', 'r').read()

def wordlist_preparation():
    words_list = []
    rough_words_list = open('words.txt', 'r').read()
    words_list = rough_words_list.split()
    return words_list

def word_random (wordlist):
    whole_list = wordlist
    rand_word = whole_list[randint(1,len(whole_list))]
    return rand_word

def word_guessing (word):
    score = 0
    word_hidden = '*' * len(word)
    letters_guessed = []
    print("\n\n\n\n\n\n\n")
    print('Your word currently is {}!'.format(word_hidden))
    while (word_hidden.find('*') >= 0):
        print("\nTell me a letter!\n")
        letter_input = input()
        print("\n\n\n\n\n\n\n")
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
    print("\nCongradulations! You guessed the word - {}. Your score is {}!".format(word, score))

def main():
    print("Welcome to Polechudes {}!\n".format(version))
    while(True):
        print("Are you ready to play? (y/n)")
        player_answer = input()
        if (player_answer == 'y'):
            word = word_random(wordlist_preparation())
            word_guessing(word)
        else:
            print("Thanks for playing!")
            break

main()