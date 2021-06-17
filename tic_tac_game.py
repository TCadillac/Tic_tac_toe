import sys

play_option = "Default"

table = {    
        " ", " ", " ",     
        " ", " ", " ",    
        " ", " ", " ", 
        }  
    

def human():
    """
    Human play option
    function called when user choose 2 players option
    """
    for turn in range(5):
        print(table)
        p1_choice = int(input("\nPlease enter a number from 1-9 to fill the table: "))
        p2_choice = int(input("\nPlease enter a number from 1-9 to fill the table: "))


def bot():
    pass


def table_update(index):
    pass

def win_check():
    # Combinations that would lead to a win
    win_list = [
        [0,1,2], [3,4,5],
        [6,7,8], [0,3,6],
        [1,4,7], [2,5,8],
        [0,4,8], [6,4,2],
    ]


while play_option.lower() != "human" and play_option.lower() != "bot":     
     play_option = input("Not a viable options, please type 'human' or 'bot': ") 
  
if play_option == "human":     
    human()
else:
    bot()