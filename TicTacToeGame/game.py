
# Game Logic File

# Create a new board


def newgame():
    board = ["", "", "",
             "", "", "",
             "", "", ""]

    turn = "X"
    return board, turn



#  Check winner


def winner(board):
    ways = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for way in ways:
        a = way[0]
        b = way[1]
        c = way[2]

        if board[a] != "" and board[a] == board[b] and board[b] == board[c]:
            return board[a]

    return ""



# Check draw


def draw(board):
    for box in board:
        if box == "":
            return False

    return True



#  Change turn


def nextturn(turn):
    if turn == "X":
        return "O"

    return "X"
