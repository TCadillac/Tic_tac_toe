import random
import sys    


def human():
    """
    Human play option, execute tic tac toe for 2 players
    function called when user choose 2 players option
    """
    table = [    
        "-", "-", "-",     
        "-", "-", "-",    
        "-", "-", "-", 
        ]
    still_game = True
    display_board(table)
    # while table still have available space, run until all boxes are filled
    while still_game:
        still_game, move_index = table_check("X", table)
        table[move_index] = "X"
        display_board(table)
        # Since while still_game can't check after the first turn, we'll need a manual check
        if still_game == True:
            still_game, move_index = table_check("O", table)
            table[move_index] = "0"
            display_board(table)
    print("DRAW!")
    retry()


def table_check(move, table) -> int:
    """
    Check tic tac toe turn, make sure no duplicate or out of range input
    """
    turn = [0,1,2,3,4,5,6,7,8]

    # - 1 to fit it to the real index of 0-8
    index = int(input("\nPlease enter a number from 1-9 to fill the table: ")) - 1

    # If there's no winner and the table has been filled:
    if len(turn) == 0:
        return False

    # If user enter invalid number or numbers that are already filled:
    while index not in turn:
        display_board(table)
        print("Not available or out of range, please try again: ")
        index = int(input("Enter a number from 1-9: ")) - 1

    turn.remove(index)
    return True, index

        
def win_check() -> bool:
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


def retry():
    answer = input("Do you want to play again? y/n: ")
    if answer.lower() == "y" or answer.lower() == "yes":
        game()
    else:
        print("You didnt enter 'y' or 'yes', so the game will end. Thanks for playing!")


def display_board(table):
    print("\n")
    print(table[0] + " | " + table[1] + " | " + table[2] + "     1 | 2 | 3")
    print(table[3] + " | " + table[4] + " | " + table[5] + "     4 | 5 | 6")
    print(table[6] + " | " + table[7] + " | " + table[8] + "     7 | 8 | 9")
    print("\n")


def game(play_option = "Blank"):
    while play_option.lower() != "human" and play_option.lower() != "bot":     
        play_option = input("Please type 'human' or 'bot': ") 
    
    if play_option == "human":     
        human()
    else:
        pass

game()