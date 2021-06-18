import random

play_option = "Default"
turn = [1,2,3,4,5,6,7,8]
table = [    
        " ", " ", " ",     
        " ", " ", " ",    
        " ", " ", " ", 
        ]       


def human():
    """
    Human play option, execute tic tac toe for 2 players
    function called when user choose 2 players option
    """
    # while table still have available space, run until all boxes are filled
    while turn:
        print(table)
        p1_choice = int(input("\nPlease enter a number from 1-9 to fill the table: "))
        table_check(p1_choice)
        table[p1_choice] = "X"
        p2_choice = int(input("\nPlease enter a number from 1-9 to fill the table: "))
        table_check(p2_choice)
        table[p2_choice] = "O"


    print("\n DRAWS! No one wins!")
    retry()


def bot():
    """
    Bot play option, execute tic tac toe for 1 players
    function called when user choose bot option
    Bot moves will be random
    """
    pass


def table_check(turn: int) -> int:
    """
    Check tic tac toe turn, make sure no duplicate
    """
    available = [0,1,2,3,4,5,6,7,8]
    if turn in available:
        available.remove(turn)
        return turn
    else:
        return None


def win_check(table = table) -> bool:
    """
    Check after every turn if a player has won
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
        print("You didnt enter y or yes, so the game will end. Thanks for playing!")


def display_board():
  print("\n")
  print(table[0] + " | " + table[1] + " | " + table[2] + "     1 | 2 | 3")
  print(table[3] + " | " + table[4] + " | " + table[5] + "     4 | 5 | 6")
  print(table[6] + " | " + table[7] + " | " + table[8] + "     7 | 8 | 9")
  print("\n")


def game(play_option):
    while play_option.lower() != "human" and play_option.lower() != "bot":     
        play_option = input("Not a viable options, please type 'human' or 'bot': ") 
    
    if play_option == "human":     
        human()
    else:
        bot()

game(play_option)