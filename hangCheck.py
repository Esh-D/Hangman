def word(guess, words, wi):
    #print(guess == words[wi])
    return(guess == words[wi])
    
def wordL(mysteryWord, answer):
    return mysteryWord == answer

def letter(guess, answer):
    #print(guess in answer)
    return guess in answer

def drawn(badGuesses, drawing):
    #print(badGuesses == len(drawing))
    return badGuesses == len(drawing)
