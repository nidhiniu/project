
# 299. Bulls and Cows
# Medium
# Topics
# Companies
# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 


def bulls_and_cows(secret_number, guessed_number):
    
    try:
        
        if not isinstance(secret_number, str) or not isinstance(guessed_number, str):
            raise ValueError("Both secret_number and guessed_number must be strings.")
        
    
        if not (secret_number.isdigit() and guessed_number.isdigit()):
            raise ValueError("Both secret_number and guessed_number must contain only digits.")
        
        
        if len(secret_number) != len(guessed_number):
            raise ValueError("The lengths of secret_number and guessed_number must be the same.")
        
    except ValueError as e:
        print(f"Error: {e}")
        return None 

    number_of_bulls = 0
    number_of_cows = 0

    
    for i in range(len(secret_number)):
        if secret_number[i] == guessed_number[i]:
            number_of_bulls += 1

    
    secret_count = {}
    guess_count = {}
    for i in range(len(secret_number)):
        secret_count[secret_number[i]] = secret_count.get(secret_number[i], 0) + 1
        guess_count[guessed_number[i]] = guess_count.get(guessed_number[i], 0) + 1

    
    for num in secret_count:
        if num in guess_count:
            number_of_cows += min(secret_count[num], guess_count[num]) - number_of_bulls

    print(f"We have the same number in the same position {number_of_bulls} times and the same number in different positions {number_of_cows} times")
    return f"{number_of_bulls}A{number_of_cows}B"



secret_number = "1123"
guessed_number = "1132"
print(bulls_and_cows(secret_number, guessed_number))
