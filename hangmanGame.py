import random
potential_words = ['example', 'cool', 'beans','spider', 'trash', 'coding', 'lunch', 'bored', 'plans', 'food', 'fruit', 'random', 'print', 'rythm', 'chocolate', 'trying something', 'two words', 'whatever']
word = random.choice(potential_words)
#word = "trying something"
word = word.lower()
guesses = []
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lives = 5
#current_word = ['_ '] *len(word)

#print(word)

while lives > 0:
    display = ""
    for letter in word:
        if letter in guesses and letter != ' ':
            display += letter
            #Could do + letter + " " and then for the win comparison create another variable that keeps track of he exact same thing witout the spaces and don't print it- then use that for the comparison.(Or could do if '_' not in display)

        #The following is for words with spaces in them. There is currently some kind of bug becasue it destroys the whole display part of the code when it's not commented out, but my brain told me that I should just leave it for now becasue it's not vital to the code. I can always do it later if I ever (haha) find myself with the motivation. Jokes! Props to Eva (GWC) for figuring out the problem. The code works when the following uses an elif instead of an if.
        elif letter == ' ':
            display += ' '
        else:
            display += '_ '
    print(display)
    if display == word:
        print("Congrats! You win!")
        break
    guess = input("Guess a letter ")
    guess = guess.lower()
    if guess.isalpha() and len(guess) == 1 and guess not in guesses:
        #alphabet.remove(guess)
        guesses.append(guess)
        print("You have guessed:",guesses)
        if guess in word:
            print('Nice')
            # current_word.insert(word.index(guess), guess)
            # current_word.remove(word.index(guess))
        else:
            print('Nope, sorry')
            lives -= 1
    else:
        print("Invalid Guess. Try Again")
    #print(alphabet)
    print(f"You have {lives} more tries")
if lives == 0:
    print(f"You lost.\nThe word is {word}.")

#Could put exit(0) at the end of the while loop instead of the last if. Didn't try it, but that's what the instructors did. Looks nicer, but I'm not in the mood to redo parts of my code lke that
