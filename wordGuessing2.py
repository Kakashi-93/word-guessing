import random
wordList = ['cat', 'car', 'rat', 'dog', 'pan', 'pen', 'fox', 'gun', 'wax']
word = random.choice(wordList)
var1 = "_"
var2 = "_"
var3 = "_"
guess = 0
guessCharacter = ""
print("""
                *******************************************************************
                *   WELCOME! To the Word Guessing game                            *
                *   Game Rules:                                                   * 
                *   1- There is a word that consist of 3 letters, try to guess    *
                *   2- You will be guessing the letters not the word              *
                *   2- If you made 5 wrong attempts you will lose                 *
                *   3- Read the previous rules carefully                          *
                *******************************************************************
                """)
while guess < 10:
    if guess < 6:
        guessCharacter = input("What is your guess? ").lower()
        # if guess is true
        if guessCharacter == word[0]:
            var1 = guessCharacter
            print("*" * 20)
            print("Your guess is right")
            print(f"The word is     {var1} {var2} {var3}")
            # check if the word was guessed successfully
            if var1 == word[0] and var2 == word[1] and var3 == word[2]:
                print("""
                                ***********************************
                                *  Congratulations you have won!  *
                                ***********************************
                                """)
                break
        # if guess is true
        elif guessCharacter == word[1]:
            var2 = guessCharacter
            print("*" * 20)
            print("Your guess is right")
            print(f"The word is     {var1} {var2} {var3}")
            # check if the word was guessed successfully
            if var1 == word[0] and var2 == word[1] and var3 == word[2]:
                print("""
                                ***********************************
                                *  Congratulations you have won!  *
                                ***********************************
                                """)
                break
        # if guess is true
        elif guessCharacter == word[2]:
            var3 = guessCharacter
            print("*" * 20)
            print("Your guess is right")
            print(f"The word is     {var1} {var2} {var3}")
            # check if the word was guessed successfully
            if var1 == word[0] and var2 == word[1] and var3 == word[2]:
                print("""
                ***********************************
                *  Congratulations you have won!  *
                ***********************************
                """)
                break
        # if guess is wrong!
        else:
            guess += 1
            print("Sorry, your guess is wrong!")
            print("*" * 20)
            print("You can try again ^_^")
            print(f"You have {5 - guess} attempts left")
            # if it is the 1st wrong attempt
            if guess == 1:
                print(
                    "         |\n"
                    "         | \n"
                    "         |\n"
                    "          ")
            # if it is the 2nd wrong attempt
            elif guess == 2:
                print("\n"
                      "         |\n"
                      "         |\n"
                      "         |\n"
                      "         |\n"
                      "         | \n"
                      "         |\n"
                      "          ")
            # if it is the 3rd wrong attempt
            elif guess == 3:
                print("\n"
                      "     ____\n"
                      "    |    |\n"
                      "    o    |\n"
                      "         |\n"
                      "         |\n"
                      "         | \n"
                      "         |\n"
                      "          ")
            # if it is the 4th wrong attempt
            elif guess == 4:
                print("\n"
                      "     ____\n"
                      "    |    |\n"
                      "    o    |\n"
                      "   /|\   |\n"
                      "         |\n"
                      "         | \n"
                      "         |\n"
                      "          ")
            # if it is the last wrong attempt
            elif guess == 5:
                print("\n"
                      "     ____\n"
                      "    |    |\n"
                      "    o    |\n"
                      "   /|\   |        GAME OVER\n"
                      "    |    |\n"
                      "   / \   | \n"
                      "         |\n"
                      "          ")
                print("""
                **************************************************
                *   Sorry, the 5 attempts are finished           *
                *   You can run the game again if you like ^_^   *
                **************************************************
                """)
                print(f"The word was {word}")
                break
