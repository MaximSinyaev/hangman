import random


def printEndGame(selectedWord, status):
    if status:
        # print(selectedWord)
        print("You guessed the word {}!".format(selectedWord))
        print("You survived!")
    else:
        print("You are hanged!")
    print()


def checkLetter(letter):
    if len(letter) != 1:
        print("You should print a single letter")
    elif not(letter.isalpha() and letter.islower()):
        print("It is not an ASCII lowercase letter")
    else:
        return letter
    return ""


def startGame(selectedWord):
    attempts = 8
    usedLetters = set()
    guessedWord = list("-" * len(selectedWord))
    while attempts:
        print()
        print("".join(guessedWord))
        # print("Input a letter: ", end='')
        letter = input("Input a letter: ")
        if checkLetter(letter) == "":
            attempts += 1
        elif letter in usedLetters:
            print("You already typed this letter")
            attempts += 1
        elif letter in selectedWord:
            for i, let in enumerate(selectedWord):
                if let == letter:
                    guessedWord[i] = let
            attempts += 1
        else:
            print("No such letter in the word")
        attempts -= 1
        usedLetters.add(letter)
        if selectedWord == "".join(guessedWord):
            printEndGame(selectedWord, 1)
            return 1
    printEndGame(selectedWord, 0)


words = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
status = input('Type "play" to play the game, "exit" to quit: ')
if status == "play":
    selectedWord = random.choice(words)
    status = startGame(selectedWord)
elif status == "exit":
    pass


