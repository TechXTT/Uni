positions = [' ' for i in range(9)]

def print_board():
    print("")
    print("+-+-+-+")
    print(f"|{positions[0]}|{positions[1]}|{positions[2]}|")
    print("+-+-+-+")
    print(f"|{positions[3]}|{positions[4]}|{positions[5]}|")
    print("+-+-+-+")
    print(f"|{positions[6]}|{positions[7]}|{positions[8]}|")
    print("+-+-+-+")
    print("")

def check_winner():
    # Check rows and columns
    for i in range(3):
        if positions[i * 3] == positions[i * 3 + 1] == positions[i * 3 + 2] != ' ':
            return positions[i * 3]
        if positions[i] == positions[i + 3] == positions[i + 6] != ' ':
            return positions[i]
    
    # Check diagonals
    if positions[0] == positions[4] == positions[8] != ' ':
        return positions[0]
    if positions[2] == positions[4] == positions[6] != ' ':
        return positions[2]
    
    return None

def minimax(depth, is_maximizing):
    winner = check_winner()
    if winner == 'O':
        return 1
    if winner == 'X':
        return -1
    if ' ' not in positions:  # Game is a tie
        return 0
    
    if depth == 0:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if positions[i] == ' ':
                positions[i] = 'O'
                score = minimax(depth - 1, False)  # Bot simulates opponent next
                positions[i] = ' '  # Undo move
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if positions[i] == ' ':
                positions[i] = 'X'
                score = minimax(depth - 1, True)  # Bot simulates itself next
                positions[i] = ' '  # Undo move
                best_score = min(score, best_score)
        return best_score

def bot_move():
    best_score = -float('inf')
    best_move = None
    
    # Iterate over all possible moves
    for i in range(9):
        if positions[i] == ' ':
            positions[i] = 'O'  # Make the move
            score = minimax(4, False)  # Evaluate the move with depth 
            positions[i] = ' '  # Undo the move
            
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move

def play_game():
    player = 'X'
    while True:
        print_board()
        if player == 'X':
            try:
                position = int(input(f"Player {player}, enter position (1-9): ").strip()) - 1
                if position not in range(9):
                    print("Invalid position. Please enter a number between 1 and 9.")
                    continue
                if positions[position] != ' ':
                    print("Position already taken.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
        else:
            position = bot_move()
            print(f"Bot chooses position {position + 1}")
        
        positions[position] = player
        winner = check_winner()
        if winner:
            print_board()
            print(f"Player {winner} wins!")
            break
        
        if ' ' not in positions:
            print_board()
            print("It's a tie!")
            break
        
        player = 'O' if player == 'X' else 'X'

play_game()