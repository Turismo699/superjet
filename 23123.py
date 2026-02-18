import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # рядки і стовпці
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # діагоналі
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def is_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def player_move(board):
    while True:
        try:
            row = int(input("Введіть рядок (0-2): "))
            col = int(input("Введіть стовпець (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Введіть числа від 0 до 2!")
                continue

            if board[row][col] != " ":
                print("Клітинка зайнята!")
                continue

            board[row][col] = "X"
            break
        except ValueError:
            print("Введіть число!")


def computer_move(board):
    print("Хід комп'ютера...")
    empty = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty.append((i, j))

    move = random.choice(empty)
    board[move[0]][move[1]] = "O"


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Гра Хрестики-Нулики")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)

        if check_winner(board, "X"):
            print("Ви перемогли!")
            break

        if is_draw(board):
            print("Нічия!")
            break

        computer_move(board)
        print_board(board)

        if check_winner(board, "O"):
            print("Комп'ютер переміг!")
            break

        if is_draw(board):
            print("Нічия!")
            break


if __name__ == "__main__":
    main()
