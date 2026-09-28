from wonderwords import RandomWord
import random

play = True

while play:

    r = RandomWord()

    deadDude0 = """
      ____
     |    |
     |    
     |   
     |    
     |   
    _|____
    
    """

    deadDude6 = """
      ____
     |    |
     |    O
     |   /|\\
     |    |
     |   / \\
    _|____
    
    """
    deadDude1 = """
      ____
     |    |
     |    O
     |   
     |    
     |   
    _|____
    
    """
    deadDude2 = """
      ____
     |    |
     |    O
     |    |
     |    
     |   
    _|____
    
    """
    deadDude3 = """
      ____
     |    |
     |    O
     |   /|
     |    
     |   
    _|____
    
    """
    deadDude4 = """
      ____
     |    |
     |    O
     |   /|\\
     |    |
     |   
    _|____
    
    """
    deadDude5 = """
      ____
     |    |
     |    O
     |   /|\\
     |    |
     |   / 
    _|____
    
    """

    secretWord = r.word()
    guessedLetters = ""
    wrongGuesses = 0

    def printhangman():
        if wrongGuesses == 0:
            print(deadDude0)
        elif wrongGuesses == 1:
            print(deadDude1)
        elif wrongGuesses == 2:
            print(deadDude2)
        elif wrongGuesses == 3:
            print(deadDude3)
        elif wrongGuesses == 4:
            print(deadDude4)
        elif wrongGuesses == 5:
            print(deadDude5)
        elif wrongGuesses == 6:
            print(deadDude6)

    def printword(word, letters):
        print("What you have so far: ", end="")
        for letter in word:
            if letter in letters:
                print(f"{letter} ", end="")
            else:
                print("_ ", end="")
        print()

    def printwrong(word, guessedLetters):
        print("Wrong guesses: ", end="")
        for guess in guessedLetters:
            if guess not in word:
                print(f"{guess} ", end="")
        print()

    def gameOver (word, guessedLetters):
        rightLetter = 0
        gameOverResponse = random.randint(0, 5)

        for letter in word:
            if letter in guessedLetters:
                rightLetter +=1
        if rightLetter == len(word):
            if gameOverResponse == 0:
                print("You win!!!")
            elif gameOverResponse == 1:
                print("Nice job I suppose")
            elif gameOverResponse == 2:
                print("I mean he's kinda alive. Missing limbs but not hanging so we can count that as a win")
            elif gameOverResponse == 3:
                print("Yeah that is the word. I don't wanna say 'won' but you didn't exactly lose so that's cool")
            elif gameOverResponse == 4:
                print("Yeah sure why not. Good job")
            else:
                print("Good job you win this time")

            print("The word was:", word)
            print()
            return True
        elif wrongGuesses == 6:
            if gameOverResponse == 0:
                print("YOU KILLED HIM!!!!")
            elif gameOverResponse == 1:
                print("L. Imagine losing to a CPU")
            elif gameOverResponse == 2:
                print("Go read the dictionary or a thesaurus or something")
            elif gameOverResponse == 3:
                print("Maybe go do something you're good at")
            elif gameOverResponse == 4:
                print("I fear the man may perchance be hanging")
            else:
                print("Skill issue")

            print("The word was:", word)
            print()
            return True
        else:
            return False

    print("Welcome to the game!")
    print("I am thinking of a word and the goal is to guess letters in the word until you get it "
          "or until all of the body parts are attached to the hangman. ")
    print("If you lose, the death is on you! Good luck :)")

    for letter in secretWord:
        print("_ ", end="")

    print()

    rightGuess = 0

    while not gameOver(secretWord, guessedLetters):
        guess = input("Guess a letter: ")
        responseNum = random.randint(0, 5)
        if guess.lower() in secretWord:
            rightGuess = 1
        else:
            rightGuess = 0
            wrongGuesses += 1

        printhangman()
        if rightGuess == 1:
            if responseNum == 0:
                print("Yup that's in there")
            elif responseNum == 1:
                print("Ooooo that'll work")
            elif responseNum == 2:
                print("Sure I suppose I can accept that")
            elif responseNum == 3:
                print("Woowwww, soooo smart")
            elif responseNum == 4:
                print("Nerd")
            else:
                print("Yeah I guess")
        else:
            if responseNum == 0:
                print("No")
            elif responseNum == 1:
                print("Nope")
            elif responseNum == 2:
                print("You aren't very good at this are you?")
            elif responseNum == 3:
                print("Loser")
            elif responseNum == 4:
                print("Maybe this is why you're adopted")
            else:
                print("Try again")
        guessedLetters = guessedLetters + guess
        printword(secretWord, guessedLetters)
        printwrong(secretWord, guessedLetters)
        print()
        print()
    playagain = input("Do you want to play again (y/n)? ")
    if playagain == "y":
        play = True
    else:
        play = False