# Hangman in Python
#  by Tim P 

import os
os.system("clear")

# Initalize
word = "UBUNTU"
guess = "------"
wrong_letters = ""

# Print Header
print("Hangman\n")

# Main game loop
while True:
    print(f"Correct Guess: {guess}")
    print(f"Wrong Guess: {wrong_letters}")

    letter = input("Please enter a letter: >\n").upper()

    # Check if letter in word
    if letter in word:
        temp = ""
        for index in range(len(word)):
            if letter == word[index]:
                temp += letter
            elif guess[index] != "-":
                temp += guess[index]
            else:
                temp += "-"
        guess = temp
    else:
        wrong_letters += letter
    
    # Check if game is won
    if word == guess:
        print("You won, have your life")
        break

    # Check if game is lost
    if len(wrong_letters) == 5:
        print("You Lose, you will be hanged")
        print(f"The correct word was {word}")
        exit()
    
    # Print Hangman
        # Print the hangman

    if len(wrong_letters) == 0:
        print("""
-------
|     
|    
|    
|    
|
|---------""")

    if len(wrong_letters) == 1:
        print("""
-------
|     O
|    
|    
|    
|
|---------""")

    if len(wrong_letters) == 2:
        print("""
-------
|     O
|     |
|     |
|    
|
|---------""")

    if len(wrong_letters) == 3:
        print("""
-------
|     O
|    \\|/
|     |
|    
|
|---------""")

    if len(wrong_letters) == 4:
        print("""
-------
|     O
|    \\|/
|     |
|    / \\
|
|---------""")
    
    if len(wrong_letters) == 5:
        print("""
-------
|     |
|     O
|    /|\\
|     |
|    | |
|---------""")
