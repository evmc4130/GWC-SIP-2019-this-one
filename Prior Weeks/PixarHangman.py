import random

HangmanWords = ["Toy Story", "A Bugs Life", "Monsters Inc", "Finding Nemo", "The Incredibles", "Cars", "Ratatouille", "WALL E", "Up", "Brave", "Monsters University", "Inside Out", "The Good Dinosaur", "Finding Dory", "Coco"]
word2 = random.choice(HangmanWords)
word2 = word2.lower()


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter_storage = []

print("P L E A S E   R E A D   T H I S !")
print("Welcome to Hangman! This was made by Eva.")
print("The theme of this hangman is 'Pixar Movies'. Good luck!")

s = "_ " * len(word2)

tries = 7

while tries > 0:
    #code for displaying
    display = ""
    for i in word2:
        if i in letter_storage:
            display += i
        elif i == ' ':
            display += ' '
        else:
            display += "_ "
    print(display)
    if display == word2:
        print("you won! the movie was", word.upper(),"!")
        break

#actual game part thingy
    print("letters guessed:", letter_storage)
    print("tries: ", tries)
    guess = input("Guess a letter: ")
    guess = guess.lower()

#proof checks if it's a valid answer
    if not guess.isalpha() or len(guess) != 1:
        print("please pick a letter from a-z.")

#when this is a valid answer it will take it out from the alphabet and put it into guesses
    elif guess.isalpha() and len(guess) == 1 and guess not in letter_storage:
        alphabet.remove(guess)
        letter_storage.append(guess)
        if guess in word:
            print("Good job!")
        else:
            tries -= 1
            print("try again!")

    elif guess in letter_storage:
            print("pick another letter, you picked that one already!")
            print(alphabet)
# now outside of the while loop, if you lose the thing below will be printed
if tries == 0:
    print("You lost :( The movie was", word.upper(),".")
    print("~ G  A  M  E    O  V  E  R ~")
