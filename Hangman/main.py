import random

print("Welcome to Hangman")
print("------------------")

WordList = ["sun", "kids", "cats", "bug", "java", "Hate", "ate", "run", "bulletproof", "kitten", "more", "later", "flower", "bulletproof"]

randomWord= random.choice(WordList)

for x in randomWord:
    print("_", end=" ")

def printhangman (wrong):
    if (wrong == 0):
        print("\n+---+")
        print("      |")
        print("      |")
        print("      |")
        print("     ===")
    elif (wrong == 1):
        print("\n+---+")
        print("  O   |")
        print("      |")
        print("      |")
        print("     ===")
    elif (wrong == 2):
        print("\n+---+")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("     ===")
    elif (wrong == 3):
        print("\n+---+")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("     ===")
    elif (wrong == 4):
        print("\n+---+")
        print("  O   |")
        print(" /|\  |")
        print("      |")
        print("     ===")
    elif (wrong == 5):
        print("\n+---+")
        print("  O   |")
        print(" /|\  |")
        print(" /    |")
        print("     ===")
    elif (wrong == 6):
        print("\n+---+")
        print("  O   |")
        print(" /|\  |")
        print(" / \  |")
        print("     ===")

def printword(guessedLetters):
    counter=0
    rightletters=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter], end=" ")
            rightletters+=1
        else:
            print(" ", end=" ")
        counter+=1
    return rightletters

def printLines():
    print("\r")
    for char in randomWord:
            print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print("\n letters guesed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    letterGuessed = input("\n Guess a letter ")
    if (randomWord[current_guess_index] == letterGuessed):
            printhangman(amount_of_times_wrong)
            current_guess_index+=1
            current_letters_guessed.append(letterGuessed)
            current_letters_right = printword(current_letters_guessed)
            printLines()
    else:
            amount_of_times_wrong +=1
            current_letters_guessed.append(letterGuessed)
            printhangman(amount_of_times_wrong)
            current_letters_right = printword(current_letters_guessed)
            printLines()

print("Game Over")
print("right word is \n")
print(randomWord)
        