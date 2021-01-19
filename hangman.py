'''
Eshika Dey
June 1 2020
CS/CE Personal Curriculum Project 1
Hangman Game -
   Notes:
   -User can only play one round and then program ends.
   -The word the user is trying to guess is hardcoded, so it will be the
   same word for every program run.
   -However, the program will work with any word of any length so you can
   manually change the word and play again
    
'''
import hangCheck
import hangDisplay

def main():
    badGuesses = 0
    drawing = (("--------------------"),
               ("             |      "),
               ("             |      "),
               ("             O      "),
               ("           / | \    "),
               ("             |      "),
               ("            / \     "),
        )

    words = ("cat", "hat", "great")
    #wi stands for word index
    wi = 0;
    answer = []
    for char in words[wi]: #cat
        answer.append(char);
        
    mysteryWord = []

    for i in range(1, len(answer) + 1):
        mysteryWord.append("_")
    #-----------------------------------------------------------------------
    #Greeting
    print("Hello! Welcome to Hangman!")
    input("Press ENTER to begin game.")
    print("__________________________________________________________________")

    while True:
        
        hangDisplay.mysteryWord(mysteryWord)
        
        choice = input("\nEnter 'l' to guess a letter.\nEnter 'w' to guess the word.\nEnter 'q' to quit program.\n")

        if (choice == "q"):
            print("Thank you for playing.")
            break
        elif (choice == "l"):
            guess = input("Enter your guess. ")
            print("__________________________________________________________________")
            
            #letter is in word
            if hangCheck.letter(guess, answer):
                mysteryWord = alterMysteryWord(answer, guess, mysteryWord)
                
                if hangCheck.wordL(mysteryWord, answer):
                    print("Congratulations, you win!")
                    break
            #letter is NOT in word
            else:
                badGuesses += 1
                hangDisplay.hangman(badGuesses, drawing)
                if hangCheck.drawn(badGuesses, drawing):
                    print("GAME OVER! You have lost.\nThe word was: " + words[wi])
                    break
            
        elif (choice == "w"):
            guess = input("Enter your guess. ")
            print("__________________________________________________________________")
            #user guess word correctly
            if hangCheck.word(guess, words, wi):
                print("Congratulations, you win!")
                break
            #user guess word INCORRECTLY
            else:
                badGuesses += 1
                hangDisplay.hangman(badGuesses, drawing)
                if hangCheck.drawn(badGuesses, drawing):
                    print("GAME OVER! You have lost. The word was: " + words[wi])
                    break
            
        else:
            print("\nI'm sorry, I didn't understand that. Please try again:")


def alterMysteryWord(answer, guess, mysteryWord):
    i = 0
    for char in answer:
        if char == guess:
            mysteryWord[i] = guess
        i += 1
    return mysteryWord
    
main()
