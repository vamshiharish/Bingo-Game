import random

def mark_values(bingo_card, value):
    for i in range(len(bingo_card)):
        for j in range(len(bingo_card[0])):
            if bingo_card[i][j] == value:
                bingo_card[i][j] = "X"
    return bingo_card

def check_bingo(bingo_card):
    rows = len(bingo_card)
    cols = len(bingo_card[0])

    # check rows
    for i in range(rows):
        row_complete = True
        for j in range(cols):
            if bingo_card[i][j] != "X":
                row_complete = False
                break
        if row_complete:
            return True

    # check columns
    for j in range(cols):
        col_complete = True
        for i in range(rows):
            if bingo_card[i][j] != "X":
                col_complete = False
                break
        if col_complete:
            return True

    # check diagonals
    diag1_complete = True
    for i in range(rows):
        if bingo_card[i][i] != "X":
            diag1_complete = False
            break
    if diag1_complete:
        return True

    diag2_complete = True
    for i in range(rows):
        if bingo_card[i][cols-i-1] != "X":
            diag2_complete = False
            break
    if diag2_complete:
        return True

    return False


def generate_bingo_card():
    numbers = random.sample(range(1, 26), 25)
    bingo_card = [numbers[i:i+5] for i in range(0, len(numbers), 5)]
    
    bingo_card[2][2] = "X"  # mark the center square as "X"
    return bingo_card

def print_bingo_card(bingo_card):
    print(" B   I   N   G   O")
    for i in range(len(bingo_card)):
        for j in range(len(bingo_card[0])):
            if bingo_card[i][j] == "X":
                print(" X ", end="")
            else:
                print(f"{bingo_card[i][j]:2d} ", end="")
        print()
def myArray(player_card):
    nested_list = []
    for i in player_card:
        for j in i:
            nested_list.append(j)   
    return nested_list          

def play_bingo():
    # generate bingo cards for player and computer
    player_card = generate_bingo_card()
    
    computer_card = generate_bingo_card()
    
    # print initial cards
    print("Player's bingo card:")
    print_bingo_card(player_card)
    print("Computer's bingo card:")
    print_bingo_card(computer_card)
    
    # game loop
    while True:
        # player's turn
        #print(player_card)
        value = int(input("Enter a value to mark on your bingo card: "))
        before_player_card = myArray(player_card)
        #print(type(value))
        if value not in before_player_card:
            print("The value is not on your bingo card. Try again.")
            continue
        player_card = mark_values(player_card, value)
        print("Your updated bingo card:")
        print_bingo_card(player_card)
        if check_bingo(player_card):
            print("BINGO! You win!")
            break

        # computer's turn
        value = random.choice([n for row in computer_card for n in row if n != "X"])
        print(f"Computer marks {value} on its bingo card.")
        computer_card = mark_values(computer_card, value)
        print("Computer's updated bingo card:")
        print_bingo_card(computer_card)
        if check_bingo(computer_card):
            print("BINGO! Computer wins!")
            break

play_bingo()



    


















          
              
                
