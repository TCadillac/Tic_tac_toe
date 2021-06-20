import random
import sys

turn = [1,2,3,4,5,6,7,8]
table = [    
        "-", "-", "-",     
        "-", "-", "-",    
        "-", "-", "-", 
        ]       


def human():
    """
    Human play option, execute tic tac toe for 2 players
    function called when user choose 2 players option
    """
    display_board()
    # while table still have available space, run until all boxes are filled
    while turn:
        p1_choice = table_check()
        table[p1_choice] = "X"
        p2_choice = table_check()
        table[p2_choice] = "O"
    retry()


def table_check() -> int:
    """
    Check tic tac toe turn, make sure no duplicate or out of range input
    """
    # - 1 to fit it to the real index of 0-8
    index = int(input("\nPlease enter a number from 1-9 to fill the table: ")) - 1
    available = [0,1,2,3,4,5,6,7,8]
    if available == False:
        win_check(False)
        sys.exit()
    while index not in available:
        display_board()
        print("Not available or out of range, please try again: ")
        index = int(input("Enter a number from 1-9: ")) - 1
    available.remove(index)
    return index


# turn_list to check for a draw, if passed and checked and avaiable moves are 0, return a draw
def win_check(turn_list = True) -> bool:
    """
    Check after every turn if a player has won, lost, or draw
    """
    # Combinations that would lead to a win
    win_list = [
        [0,1,2], [3,4,5],
        [6,7,8], [0,3,6],
        [1,4,7], [2,5,8],
        [0,4,8], [6,4,2],
    ]
    if turn_list == False:
        print("DRAW!")
        retry()

def retry():
    answer = input("Do you want to play again? y/n: ")
    if answer.lower() == "y" or answer.lower() == "yes":
        game()
    else:
        print("You didnt enter 'y' or 'yes', so the game will end. Thanks for playing!")


def display_board():
  print("\n")
  print(table[0] + " | " + table[1] + " | " + table[2] + "     1 | 2 | 3")
  print(table[3] + " | " + table[4] + " | " + table[5] + "     4 | 5 | 6")
  print(table[6] + " | " + table[7] + " | " + table[8] + "     7 | 8 | 9")
  print("\n")


def game(play_option = "Blank"):
    while play_option.lower() != "human" and play_option.lower() != "bot":     
        play_option = input("Not a viable option, please type 'human' or 'bot': ") 
    
    if play_option == "human":     
        human()
    else:
        pass

game()