import sys

def checkmate(board: str):
    board = board.replace('\r', '').strip().split('\n')
    size = len(board)

    if size == 0 or any(len(row) != size for row in board):
        print("Error")
        return

    king_positions = [(i, j)
                      for i in range(size)
                      for j in range(size)
                      if board[i][j] == 'K']

    if len(king_positions) != 1:
        print("Error")
        return

    king_x, king_y = king_positions[0]

    def in_bounds(x, y):
        return 0 <= x < size and 0 <= y < size

    def is_pawn_attacking():
        for dx, dy in [(1, -1), (1, 1)]:  # <<< แก้ตรงนี้
            nx, ny = king_x + dx, king_y + dy
            if in_bounds(nx, ny) and board[nx][ny] == 'P':
                return True
        return False

    def is_bishop_attacking():
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = king_x + dx, king_y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece in 'BQ':
                    return True
                else:
                    break
        return False

    def is_rook_attacking():
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = king_x + dx, king_y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece in 'RQ':
                    return True
                else:
                    break
        return False

    if is_pawn_attacking() or is_bishop_attacking() or is_rook_attacking():
        print("Success")
    else:
        print("Fail")


def main():
    if len(sys.argv) < 2:
        print("Error")
        return

    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as f:
                board = f.read()
                if not board.strip():
                    print("Error")
                    continue
                checkmate(board)
        except:
            print("Error")

if __name__ == "__main__":
    main()
