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

Personal Feedback:
    -My solution and the implementation process of that solution was disorganized,
    I should have spent more time in the planning stage (Analysis & Design) so
    that the Implementation stage would have gone smoother and I would have had a
    clearer idea of how the program would work
    
    -I broke the problem into seperate pieces but I didn't plan out what I was
    going to implement first and then second, etc. I should have done that, less
    confusion and would have finished faster

    -I shouldn't rush ahead of the planning process and into implementation even if I
    think a project is "easy", like I did with this one. This goes to show that even 
    simple projects can confuse you if you aren't mentally clear on how you are going
    to implement something
        - This confusion / vagueness will be worse for larger more complex projects
        - I did finish it though, because again it is an easy program to make, but I
        don't think it is the best solution I could have made and it took me longer to
        implement than I thought it would

    -My focus with these projects should be to strengthen my coding process
        - Truly understanding the project and my plan before jumping in
        - Basically: have a more logical, organized, and clear workflow
        - Aim is to create great solutions with reduced implementation time

        - Clearly identify "This is what I'm setting out to do, this is how I'm going
        to do it, and then do it"
    
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
