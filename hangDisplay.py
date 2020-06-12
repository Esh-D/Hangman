def mysteryWord(mysteryWord):
    print("\nGuess the word below: ")
    for char in mysteryWord:
        print(char, end=" ")
    print()
def hangman(badGuesses, drawing):
    print("Hangman Drawing:")
    for i in range(0, badGuesses):
        print(drawing[i])
