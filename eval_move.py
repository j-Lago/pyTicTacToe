def eval_move(board: list[list[int]], r, c) -> tuple[list[list[int]], int]:
    bsum = board_sum(board)
    if board[r][c] == 0:
        board[r][c] = 1 if bsum == 0 else -1
    result = h_check(board) + v_check(board) + d_check(board)

    if result == 0 and full_check(board):
        result = 2
    return board, result


def board_sum(board):
    bsum = 0
    for row_elements in board:
        bsum += sum(row_elements)
    return bsum


def validate(board):
    return board_sum(board) <= 1


def h_check(board) -> int:
    for r in range(3):
        cum = 0
        for c in range(3):
            cum += board[r][c]
        if cum == 3:
            return 1
        if cum == -3:
            return -1
    return 0


def v_check(board) -> int:
    for c in range(3):
        cum = 0
        for r in range(3):
            cum += board[r][c]
        if cum == 3:
            return 1
        if cum == -3:
            return -1
    return 0


def full_check(board) -> bool:
    for c in range(3):
        for r in range(3):
            if board[r][c] == 0:
                return False
    return True


def d_check(board) -> int:
    cum1 = board[0][0] + board[1][1] + board[2][2]
    cum2 = board[2][0] + board[1][1] + board[0][2]
    if cum1 == 3 or cum2 == 3:
        return 1
    if cum1 == -3 or cum2 == -3:
        return -1
    return 0