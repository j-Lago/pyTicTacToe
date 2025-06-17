from outcome_convention import Outcome

BoardSateType = list[list[int]]


def eval_move(board: BoardSateType, next_move: tuple[int, int]) -> tuple[BoardSateType, Outcome]:

    if not validate(board):
        return board, Outcome.INVALID_STATE

    r, c = next_move
    if board[r][c] == 0:
        board[r][c] = 1 if board_sum(board) == 0 else -1
    else:
        return board, Outcome.INVALID_MOVE

    if (outcome := h_check(board)) != Outcome.CONTINUE: return board, outcome
    if (outcome := v_check(board)) != Outcome.CONTINUE: return board, outcome
    if (outcome := d_check(board)) != Outcome.CONTINUE: return board, outcome
    if full_check(board): return board, Outcome.DRAW

    return board, Outcome.CONTINUE


def board_sum(board):
    bsum = 0
    for row_elements in board:
        bsum += sum(row_elements)
    return bsum


def validate(board):
    return board_sum(board) <= 1


def h_check(board) -> Outcome:
    for r in range(3):
        cum = 0
        for c in range(3):
            cum += board[r][c]
        if cum == 3:
            return Outcome.X_WINS
        if cum == -3:
            return Outcome.O_WINS
    return Outcome.CONTINUE


def v_check(board) -> Outcome:
    for c in range(3):
        cum = 0
        for r in range(3):
            cum += board[r][c]
        if cum == 3:
            return Outcome.X_WINS
        if cum == -3:
            return Outcome.O_WINS
    return Outcome.CONTINUE


def full_check(board) -> bool:
    for c in range(3):
        for r in range(3):
            if board[r][c] == 0:
                return False
    return True


def d_check(board) -> Outcome:
    cum1 = board[0][0] + board[1][1] + board[2][2]
    cum2 = board[2][0] + board[1][1] + board[0][2]
    if cum1 == 3 or cum2 == 3:
        return Outcome.X_WINS
    if cum1 == -3 or cum2 == -3:
        return Outcome.O_WINS
    return Outcome.CONTINUE