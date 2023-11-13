board = [
    ["_ ", "_ ", "_ "],
    ["_ ", "_ ", "_ "],
    ["_ ", "_ ", "_ "]
]
player = "X"
turns = 1

while turns < 10:
    print("Player " + player + "\'s turn:")
    row = int(input("What row? (0, 1, 2)"))
    col = int(input("What column? (0, 1, 2)"))

    if row >= 3 or col >= 3:
        print("Invalid input. Please select appropriate rows/columns.")
        continue  # Added to restart the loop if the input is invalid

    if board[row][col] == "_ ":  # Check if the cell is empty
        board[row][col] = player

        for r in board:
            for c in r:
                print(c, end="")
            print()
        turns += 1

        # Switch players for the next turn
        if player == "X":
            player = "0"
        else:
            player = "X"
    else:
        print("Cell already occupied. Please choose another.")
