
import random

board = [' '] * 9
computer = 'X'
player = 'O'

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print(f"___|___|___")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print(f"___|___|___")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print(f"   |   |  ")
    print()

def win_checking():
    
    winning_combinations = [
        [0, 1, 2],  
        [3, 4, 5],  
        [6, 7, 8], 
        [0, 3, 6], 
        [1, 4, 7], 
        [2, 5, 8], 
        [0, 4, 8], 
        [6, 4, 2]      ]
    
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return True
            
    return False

def check_position(position):
    return board[position] == ' '

def draw_checking():
    return ' ' not in board

def player_move(letter):
    while True:
        try:
            position = int(input("Enter the position you want to choose from 0 to 8: "))
            if check_position(position):
                insert(letter, position)
                break
            else:
                print("Position is not available, re-enter the position.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 8.")

def computer_move(letter):
    while True:
        position = random.randint(0, 8)
        if check_position(position):
            insert(letter, position)
            break

def insert(letter, position):
    board[position] = letter
    display_board(board)
    if win_checking():
        if letter == 'X':
            print("Computer wins!!!!")
            exit()
        else:
            print("Player wins!!!!!")
            exit()


while True:
    display_board(board)
    player_move(player)
    if win_checking() or draw_checking():
        if draw_checking():
            print("The game is a draw!!!")
        break
    
    computer_move(computer)
    if win_checking() or draw_checking():
        if draw_checking():
            print("The game is a draw!!!")
        break


