import random

# --- Define your functions below! ---
def greet():
    greetings = ["Howdy!", "Hey, there!", "Hello!", "Hey man.", "What's poppin' Jimbo?"]
    print(random.choice(greetings))
    name = input("What's your name? ")

    print("Hello %s! My name is Sally!" %name)

def feeling():
    feelings = ["happy!", "tired.", "just peachy!", "hungry!!!!!!", "quite fine"]
    compfeels = random.choice(feelings)
    stories = ["When the coder who coded this was walking to Morgan Stanley the other day, she totally got Regina Georged.", "WHAT IF I TOLD YOU I STOLE A CARDBOARD CUTOUT OF DANNY DEVITO?", "Once upon a time  group of adevnturers went on an adventure to the fridge, they returned with cookies and milk. \nThe end."]
    randomstories = random.choice(stories)
    feel = input("How are you feeling this fine afternoon? ")
    if feel.lower() == "good":
        print("So glad to hear that! I'm feeling", compfeels)
    elif feel.lower() == "bad":
        story = input("I'm so sorry to hear that! Would you like for me to tell you a story to make you feel better? y/n: ")
        if story.lower() == "y" or story.lower() == "yes":
            print(randomstories)
        elif story.lower() == "n" or story.lower() == "no":
            print("Okay, I hope you feel better soon.")
        else:
            print("SALLY DOES NOT UNDERSTAND SALLY GOES HOME NOW.")

    else:
        print("Yeah, me too.")
def talk():
    randomfoods = ["Good choice! My favorite food is mac and cheese!", "I hate mayonnaise", "Soda makes my keys sticky", "Water makes me short circuit"]
    foodopinion = random.choice(randomfoods)
    topic = input("What do you want to talk about? (ex: music, food, colors, etc.) ")
    topic = topic.lower()
    if topic == "food":
        print(foodopinion)
    elif topic == "colors":
        color =input("What's your favorite color? ")
        if color.lower() == "blue":
            print("I also love blue! Especially the blue sky")
        else:
            print("Nice!")
    elif topic == 'music':
        genre = input("What music do you like? ")
        genre = genre.lower()
        if genre == "pop":
            print("Same! I like Billie Eilish and Ed Sheeran!")
        elif genre == "alternative":
            print("Cool! I like Panic! At the Disco and the 1975!")
        else:
            print("Me too!")
    else:
        print("Sounds cool!")
def school():
    subject = input("What's your favorite subject in school? ")
    why = input("Cool! Why do you like %s? " %subject)
    print("Good point. I like computer science class the best")
def game():
    potential_words = ['example', 'cool', 'beans','spider', 'trash', 'coding', 'lunch', 'bored', 'plans', 'food', 'fruit', 'random', 'print', 'rythm', 'chocolate', 'trying something', 'two words', 'whatever']
    word = random.choice(potential_words)
    word = word.lower()
    guesses = []
    lives = 5
    hangmanWords = ["Toy Story", "A Bugs Life", "Monsters Inc", "Finding Nemo", "The Incredibles", "Cars", "Ratatouille", "WALL E", "Up", "Brave", "Monsters University", "Inside Out", "The Good Dinosaur", "Finding Dory", "Coco"]
    word2 = random.choice(hangmanWords)
    word2 = word2.lower()
    s = "_ " * len(word2)
    tries = 7
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter_storage = []
    moreHangmanWords = ["Snow White and the Seven Dwarfs", "Pinocchio", "Fantasia", "Dumbo", "Bambi",  "Saludos Amigos", "The Three Caballeros", "Make Mine Music", "Fun and Fancy Free", "Melody Time", "The Adventures of Ichabod and Mr Toad", "Cinderella", "Alice in Wonderland", "Peter Pan", "Lady and the Tramp", "Sleeping Beauty", "One Hundred and One Dalmatians", "Sword in the Stone", "The Jungle Book", "The Aristocats", "Robin Hood", "The Mnay Adventures of Winnie the Pooh", "The Rescuers", "The Fox and the Hound", "The Black Cauldron", "The Great Mouse Detective", "Oliver and Company", "The Little Mermaid","The Rescuers Down Under","Beauty and the Beast", "Aladdin", "The Lion King", "Pocahontas", "The Hunchback of Notre Dame", "Hercules", "Mulan", "Tarzan", "Dinosaur", "The Emperors New Groove", "Atlantis The Lost Empire", "Lilo and Stitch", "Treasure Planet", "Brother Bear", "Home on the Range", "Chicken Little", "Meet the Robinsons", "Bolt", "Princess and the Frog", "Winnie the Pooh", "Wreck it Ralph", "Frozen", "Big Hero Six", "Zootopia", "Moana", "Ralph Breaks the Internet"]

    word3 = random.choice(moreHangmanWords)
    word3 = word3.lower()
    s = "_ " * len(word3)
    wives = 7
    letter_storage2 = []
    play = input("Do you want to play a game? ")
    play = play.lower()
    if play == "yes":
        type = input("Number Game or Hangman? ")
        type = type.lower()

        if type == "number game":
            number = random.randint(1,20)
            chances = 5
            while chances > 0:
                print("chances:",chances)
                guess = input("Guess a number from 1 to 20: ")
                if not guess.isnumeric():
                    continue
                if int(guess) == number:
                    print("You win!")
                    reply = input("Do you want to play again or another game? yes/no: ")
                    if reply.lower() == "yes" :
                        while True:
                            game()
                    elif reply.lower() == "no":
                        print("okay, that's fine.")
                        print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
                        break
                elif int(guess) > number:
                    chances -= 1
                    print("Your guess was too high")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~")
                elif int(guess) < number:
                    chances -= 1
                    print("Your guess was too low")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~")
                elif chances == 0:
                    print("You Lose. The number was:", number)
                    reply = input("Do you want to play again or another game? yes/no: ")
                    if reply.lower() == "yes" :
                        while True:
                            game()
                    elif reply.lower() == "no":
                        print("okay, that's fine.")
                        print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
                else:
                    print("I do not compute.")

        elif type == "hangman":
            hangman = input("Disney, Pixar or regular? ")
            hangman = hangman.lower()

            if hangman == "pixar":
                while tries > 0:
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
                        print("you won! the movie was", word2.upper(),"!")
                        reply = input("Do you want to play again or another game? yes/no: ")
                        if reply.lower() == "yes" :
                            while True:
                                game()
                        elif reply.lower() == "no":
                            print("okay, that's fine.")
                            print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
                            break
                    print("letters guessed:", letter_storage)
                    print("tries: ", tries)
                    guess = input("Guess a letter: ")
                    guess = guess.lower()
                    if not guess.isalpha() or len(guess) != 1:
                        print("please pick a letter from a-z.")
                    elif guess.isalpha() and len(guess) == 1 and guess not in letter_storage:
                        alphabet.remove(guess)
                        letter_storage.append(guess)
                        if guess in word2:
                            print("Good job!")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~")
                        else:
                            tries -= 1
                            print("try again!")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~")
                    elif guess in letter_storage:
                            print("pick another letter, you picked that one already!")
                            print(alphabet)
                if tries == 0:
                    print("You lost :( The movie was", word2.upper(),".")
                    print("~ G  A  M  E    O  V  E  R ~")
                    reply = input("Do you want to play again or another game? yes/no: ")
                    if reply.lower() == "yes" :
                        while True:
                            game()
                    elif reply.lower() == "no":
                        print("okay, that's fine.")
                        print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

            elif hangman == "regular":
                while lives > 0:
                    display = ""
                    for letter in word:
                        if letter in guesses and letter != ' ':
                            display += letter
                        elif letter == ' ':
                            display += ' '
                        else:
                            display += '_ '
                    print(display)
                    if display == word:
                        print("Congrats! You win!")
                        reply = input("Do you want to play again or another game? yes/no: ")
                        if reply.lower() == "yes" :
                            while True:
                                game()
                        elif reply.lower() == "no":
                            print("okay, that's fine.")
                            print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
                            break
                    guess = input("Guess a letter ")
                    guess = guess.lower()
                    if guess.isalpha() and len(guess) == 1 and guess not in guesses:
                        guesses.append(guess)
                        print("You have guessed:",guesses)
                        if guess in word:
                            print('Nice')
                        else:
                            print('Nope, sorry')
                            lives -= 1
                    else:
                        print("Invalid Guess. Try Again")
                    print(f"You have {lives} more tries")
                if lives == 0:
                    print(f"You lost.\nThe word is {word}.")
                    reply = input("Do you want to play again or another game? yes/no: ")
                    if reply.lower() == "yes" :
                        while True:
                            game()
                    elif reply.lower() == "no":
                        print("okay, that's fine.")
                        print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
            elif hangman == "disney":
                while wives > 0:
                    display = ""
                    for i in word3:
                        if i in letter_storage2:
                            display += i
                        elif i == ' ':
                            display += ' '
                        else:
                            display += "_ "
                    print(display)
                    if display == word3:
                        print("you won! the movie was", word3.upper(),"!")
                        reply = input("Do you want to play again or another game? yes/no: ")
                        if reply.lower() == "yes" :
                            while True:
                                game()
                        elif reply.lower() == "no":
                            print("okay, that's fine.")
                            print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
                            break
                    print("letters guessed:", letter_storage2)
                    print("tries: ", wives)
                    guess = input("Guess a letter: ")
                    guess = guess.lower()
                    if not guess.isalpha() or len(guess) != 1:
                        print("please pick a letter from a-z.")
                    elif guess.isalpha() and len(guess) == 1 and guess not in letter_storage2:
                        alphabet.remove(guess)
                        letter_storage2.append(guess)
                        if guess in word3:
                            print("Good job!")
                        else:
                            wives -= 1
                            print("try again!")
                    elif guess in letter_storage2:
                            print("pick another letter, you picked that one already!")
                if wives == 0:
                    print("You lost :( The movie was", word3.upper(),".")
                    print("~ G  A  M  E    O  V  E  R ~")
                    reply = input("Do you want to play again or another game? yes/no: ")
                    if reply.lower() == "yes" :
                        while True:
                            game()
                    elif reply.lower() == "no":
                        print("okay, that's fine.")
                        print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

            else:
                print("I do not compute")
                while True:
                    game()
    elif play == "no":
        print("Okay. We don't have to.")
    else:
        print("Sorry, what?")
        while True:
            game()


# --- Put your main program below! ---
def main():
    greet()
    feeling()
    while True:
        talk()
        school()
        game()



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
