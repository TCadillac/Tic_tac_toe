table = {    
    " ", " ", " ",     
    " ", " ", " ",    
    " ", " ", " ", 
    }  

play_option = input("Play with bot or human? ") 

while play_option.lower() != "human" and play_option.lower() != "bot":     
     play_option = input("Not a viable options, please type 'human' or 'bot': ") 
  
def human():
    print(table)
    p1_choice = int(input("\nPlease enter a number from 1-9 to fill the table: "))
    p2_choice = int(input("\nPlease enter a number from 1-9 to fill the table: "))

if play_option == "human":     
    human()
else:
    bot()

def win_check():
    # Combinations that would lead to a win
    win_list = [
        [0,1,2], [3,4,5],
        [6,7,8], [0,3,6],
        [1,4,7], [2,5,8],
        [0,4,8], [6,4,2],
    ]
    if table