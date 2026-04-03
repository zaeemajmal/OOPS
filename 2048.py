import random

print("Welcome to 2048 game")
print("Instructions:-")
print("""Controls:-
      W/w for up, A/a for left, S/s for down and D/d for right
How to Play:-
      When two tiles with the same number collide, they merge into one with their total value (e.g., 2 + 2 = 4).
      Every move spawns a new tile (usually a 2 or 4) in a random empty spot on the grid.
      Keep merging tiles and try to reach the 2048 tile to win. 
      You can keep playing for a higher score even after reaching 2048!
      If the board fills up and no more moves are possible, the game is over.
      The board is a 4x4.
Tip : Put The Terminal in full screen! 
ENJOY THE GAME!
""")

Score = 0

def print_board():
    print("\nScore :- ", Score)
    print(f"{The_Board['A1']}   {The_Board['A2']}   {The_Board['A3']}   {The_Board['A4']}\n")
    print(f"{The_Board['B1']}   {The_Board['B2']}   {The_Board['B3']}   {The_Board['B4']}\n")
    print(f"{The_Board['C1']}   {The_Board['C2']}   {The_Board['C3']}   {The_Board['C4']}\n")
    print(f"{The_Board['D1']}   {The_Board['D2']}   {The_Board['D3']}   {The_Board['D4']}")

def spawn_tile():
    empty = []
    for key in Board_Keys:
        if The_Board[key] == 0:
            empty.append(key)
    if empty:
        s = random.choice(empty)
        The_Board[s] = random.choice([2, 4])

def move_row(row):
    global Score
    new_row = []
    for num in row:
        if num != 0:
            new_row.append(num)
    i = 0
    while i < len(new_row) - 1:
        if new_row[i] == new_row[i+1]:
            new_row[i] *= 2
            Score += new_row[i]
            new_row[i+1] = 0
            i += 1
        i += 1
    final_row = []
    for num in new_row:
        if num != 0:
            final_row.append(num)
    while len(final_row) < 4:
        final_row.append(0)
    return final_row

def board_to_grid():
    return [
        [The_Board['A1'], The_Board['A2'], The_Board['A3'], The_Board['A4']],
        [The_Board['B1'], The_Board['B2'], The_Board['B3'], The_Board['B4']],
        [The_Board['C1'], The_Board['C2'], The_Board['C3'], The_Board['C4']],
        [The_Board['D1'], The_Board['D2'], The_Board['D3'], The_Board['D4']]
    ]

def grid_to_board(grid):
    keys = [
        ['A1','A2','A3','A4'],
        ['B1','B2','B3','B4'],
        ['C1','C2','C3','C4'],
        ['D1','D2','D3','D4']
    ]
    for i in range(4):
        for j in range(4):
            The_Board[keys[i][j]] = grid[i][j]

def board_changed(old, new):
    for i in range(4):
        for j in range(4):
            if old[i][j] != new[i][j]:
                return True
    return False

def move(direction):
    grid = board_to_grid()
    old_grid = [row[:] for row in grid]

    if direction == "a":
        for i in range(4):
            grid[i] = move_row(grid[i])

    elif direction == "d":
        for i in range(4):
            grid[i].reverse()
            grid[i] = move_row(grid[i])
            grid[i].reverse()

    elif direction == "w":
        for j in range(4):
            col = []
            for i in range(4):
                col.append(grid[i][j])
            col = move_row(col)
            for i in range(4):
                grid[i][j] = col[i]

    elif direction == "s":
        for j in range(4):
            col = []
            for i in range(4):
                col.append(grid[i][j])
            col.reverse()
            col = move_row(col)
            col.reverse()
            for i in range(4):
                grid[i][j] = col[i]

    if board_changed(old_grid, grid):
        grid_to_board(grid)
        spawn_tile()

def is_game_over():
    for key in Board_Keys:
        if The_Board[key] == 0:
            return False
    grid = board_to_grid()
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                return False
    for j in range(4):
        for i in range(3):
            if grid[i][j] == grid[i+1][j]:
                return False
    return True

def check_win():
    for key in Board_Keys:
        if The_Board[key] == 2048:
            return True
    return False

The_Board = {"A1":0,"A2":0,"A3":0,"A4":0,
             "B1":0,"B2":0,"B3":0,"B4":0,
             "C1":0,"C2":0,"C3":0,"C4":0,
             "D1":0,"D2":0,"D3":0,"D4":0}

Board_Keys = ["A1","A2","A3","A4",
              "B1","B2","B3","B4",
              "C1","C2","C3","C4",
              "D1","D2","D3","D4"]

spawn_tile()

while True:
    print_board()
    move_input = input("Enter move (W/A/S/D): ").lower()

    if move_input not in ["w","a","s","d"]:
        print("Invalid input!")
        continue

    move(move_input)

    if check_win():
        print_board()
        print("YOU REACHED 2048! YOU WIN!")
        choice = input("Continue playing? (y/n): ").lower()
        if choice != "y":
            break

    if is_game_over():
        print_board()
        print("Game Over!")
        break

    