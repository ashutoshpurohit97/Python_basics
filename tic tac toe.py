import itertools

def game_board(game_map,player=0,row = 0,column = 0, just_display = False):
    if game_map[row][column] != 0
        print("This poso=ition is occupied ! Choose another one. ")
        return False
    try:
        print('   a  b  c ')
        if not just_display:
            game_map[row][column] = player
        for count,row in enumerate(game_map):
                print(count,row)
        return game_map
    except IndexError as e:
        print("Make sure that you put row/column as 0, 1 or 2")
        return False
    except Exception as e: 
        print("Oops! Something went wrong!")
        return False



def win(current_game):
    #Horizontal winner
    for row in game:
        #print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the Winner Horizontally !")

    #Vertical winner
    for col in range(len(game)):
        check = []

        for row in game:
        #print(row)
            check.append(row[col])
        if check.count(check[col]) == len(check) and check != 0:
            print(f"Player {check[0]} is the Winner Vertically !")

    #Left Diagonal Winner
    diagsl = []
    for ix in range(len(game)):
        diagsl.append(game[ix][ix])
    if diagsl.count(diagsl[0]) == len(diagsl) and diagsl[0] != 0:
        print(f"Player {diagsl[0]} is the Winner Left diagonally !")

    #Right Diagonal winner
    diagsr = []
    for col,row in enumerate(reversed(range(len(game)))):
        diagsr.append(game[row][col])
    if diagsr.count(diagsr[0]) == len(diagsr) and diagsr[0] != 0:
        print(f"Player {diagsr[0]} is the Winner Right diagonally !")


play =  True
players = [1,2]

while play:
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    game_won = False
    game = game_board(game, just_display = True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player : {current_player}")
        row_choice = int(input("Which row you want to play ? (0,1,2): "))
        col_choice = int(input("Which column you want to play ? (0,1,2): "))
        game = game_board(game, current_player, row_choice,col_choice)
