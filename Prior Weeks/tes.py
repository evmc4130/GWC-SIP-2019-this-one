# ages = [18, 20, 21]
# sum = 0
# for i in range(3):
#     sum += ages[i]
#
#
# avg = sum/len(ages)
# print(avg)

#
#
# if type == "number game":
#     number = random.randint(1,20)
#     chances = 5
#     while chances > 0:
#         print(chances)
#         guess = input("Guess a number from 1 to 20")
#         if int(guess) == number:
#             print("You win!")
#         elif int(guess) > number:
#             chances -= 1
#             print("Your guess was too high")
#         elif int(guess) < number:
#             chances -= 1
#             print("Your guess was too low")
#         elif chances == 0:
#             print("You Lose. The number was:", number)
# else:
#             print("I do not compute.")






import random

moreHangmanWords = ["Snow White and the Seven Dwarfs", "Pinocchio", "Fantasia", "Dumbo", "Bambi",  "Saludos Amigos", "The Three Caballeros", "Make Mine Music", "Fun and Fancy Free", "Melody Time", "The Adventures of Ichabod and Mr Toad", "Cinderella", "Alice in Wonderland", "Peter Pan", "Lady and the Tramp", "Sleeping Beauty", "One Hundred and One Dalmatians", "Sword in the Stone", "The Jungle Book", "The Aristocats", "Robin Hood", "The Mnay Adventures of Winnie the Pooh", "The Rescuers", "The Fox and the Hound", "The Black Cauldron", "The Great Mouse Detective", "Oliver and Company", "The Little Mermaid","The Rescuers Down Under","Beauty and the Beast", "Aladdin", "The Lion King", "Pocahontas", "The Hunchback of Notre Dame", "Hercules", "Mulan", "Tarzan", "Dinosaur", "The Emperors New Groove", "Atlantis The Lost Empire", "Lilo and Stitch", "Treasure Planet", "Brother Bear", "Home on the Range", "Chicken Little", "Meet the Robinsons", "Bolt", "Princess and the Frog", "Winnie the Pooh", "Wreck it Ralph", "Frozen", "Big Hero Six", "Zootopia", "Moana", "Ralph Breaks the Internet"]

word3 = random.choice(moreHangmanWords)
word3 = word3.lower()
s = "_ " * len(word3)
wives = 7
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter_storage2 = []



hangman = input("input disney")


if hangman == "disney":
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
    print("oof")
