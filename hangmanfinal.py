import random

def movie():
    movies = ["lucifer", "lost", "friends","dexter","got","breakingbad","prisonbreak"]
    return random.choice(movies)

def play_game():


    def try_one_more():
        try_again=int(input("Do you want to play again??? if yes,enter: 1, else enter :0  :::"))
        if try_again==1:
            play_game()
        else:
            return
    chance = 8
    word = movie()
    guessed_letters = []  
    word_length = len(word)

    print(f"The selected  word has {word_length} letters,you can start guessing now:::")
    
    while chance > 0  :
        
        current_state = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Current word: ", current_state)
        
        if current_state == word:  
            print("You got it correct and you  won!")
            try_one_more()
            return
        
        guess = input("Enter your guess,one letter at a time ").lower()
        
        if len(guess) != 1: 
            print("Please enter only one letter.")

            continue
        if guess.isnumeric == True:
            print("Please enter alphabets only")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)  
        
        if guess not in word:
            chance -= 1
            print(f"Incorrect guess! You have {chance} chances left.")
        else:
            print("Good guess!")

    print(f"You lost! The word was '{word}'.")
    try_one_more()
    
play_game()