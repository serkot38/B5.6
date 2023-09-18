cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def print_cells():
    print(cells[0], end=" ")
    print(cells[1], end=" ")
    print(cells[2])

    print(cells[3], end=" ")
    print(cells[4], end=" ")
    print(cells[5])

    print(cells[6], end=" ")
    print(cells[7], end=" ")
    print(cells[8])


def step_cells(step, symbol):
    i = cells.index(step)
    cells[i] = symbol


def result():
    win = ""

    for i in wins:
        if cells[i[0]] == "X" and cells[i[1]] == "X" and cells[i[2]] == "X":
            win = "Игрок 1"
        if cells[i[0]] == "O" and cells[i[1]] == "O" and cells[i[2]] == "O":
            win = "Игрок 2"
    return win


game_over = False
player1 = True

while not game_over:
    print_cells()
    if player1:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))

    step_cells(step, symbol)
    win = result()
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not player1

print_cells()
print("Победил", win)
