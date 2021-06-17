import sys

play_option = "Default"
table = {    
        " ", " ", " ",     
        " ", " ", " ",    
        " ", " ", " ", 
        }  


def human():
    """
    Human play option, execute tic tac toe for 2 players
    function called when user choose 2 players option
    """
    # Total move it takes to complete the table in turn
    for turn in range(5):
        print(table)
        p1_choice = int(input("\nPlease enter a number from 1-9 to fill the table: "))
        p2_choice = int(input("\nPlease enter a number from 1-9 to fill the table: "))

    print("\n DRAWS! No one wins!")
    retry()


def bot():
    """
    Bot play option, execute tic tac toe for 1 players
    function called when user choose bot option
    !!! Bot moves will be random
    """
    pass


def table_update(first, second, table = table):
    """
    Update tic tac toe table, takes in 2 turn at once
    Run first turn first, then second
    """
    return table


def win_check(table = table):
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


def game():
    while play_option.lower() != "human" and play_option.lower() != "bot":     
        play_option = input("Not a viable options, please type 'human' or 'bot': ") 
    
    if play_option == "human":     
        human()
    else:
        bot()

game()