from core.constants import (
    WHITE, BLACK, EMPTY,
    KING_DIRECTIONS, KNIGHT_DELTAS, SLIDING_RAYS, MOVE_GENERATORS,
)


def generate_pawn_moves(board, r, c, captures_only=False):
    moves = []
    piece = board.board[r][c]

    if piece == 'P':
        if not captures_only:
            if r - 1 >= 0 and board.board[r - 1][c] == EMPTY:
                if r - 1 == 0:
                    for p in ['Q', 'R', 'B', 'N']:
                        moves.append((r, c, r - 1, c, p))
                else:
                    moves.append((r, c, r - 1, c))

                if r == 6 and board.board[r - 2][c] == EMPTY:
                    moves.append((r, c, r - 2, c))

        if r - 1 >= 0 and c - 1 >= 0 and board.is_black(board.board[r - 1][c - 1]):
            if r - 1 == 0:
                for p in ['Q', 'R', 'B', 'N']:
                    moves.append((r, c, r - 1, c - 1, p))
            else:
                moves.append((r, c, r - 1, c - 1))

        if r - 1 >= 0 and c + 1 < 8 and board.is_black(board.board[r - 1][c + 1]):
            if r - 1 == 0:
                for p in ['Q', 'R', 'B', 'N']:
                    moves.append((r, c, r - 1, c + 1, p))
            else:
                moves.append((r, c, r - 1, c + 1))

    elif piece == 'p':
        if not captures_only:
            if r + 1 < 8 and board.board[r + 1][c] == EMPTY:
                if r + 1 == 7:
                    for p in ['Q', 'R', 'B', 'N']:
                        moves.append((r, c, r + 1, c, p))
                else:
                    moves.append((r, c, r + 1, c))

                if r == 1 and board.board[r + 2][c] == EMPTY:
                    moves.append((r, c, r + 2, c))

        if r + 1 < 8 and c - 1 >= 0 and board.is_white(board.board[r + 1][c - 1]):
            if r + 1 == 7:
                for p in ['Q', 'R', 'B', 'N']:
                    moves.append((r, c, r + 1, c - 1, p))
            else:
                moves.append((r, c, r + 1, c - 1))

        if r + 1 < 8 and c + 1 < 8 and board.is_white(board.board[r + 1][c + 1]):
            if r + 1 == 7:
                for p in ['Q', 'R', 'B', 'N']:
                    moves.append((r, c, r + 1, c + 1, p))
            else:
                moves.append((r, c, r + 1, c + 1))

    return moves


def generate_knight_moves(board, r, c, captures_only=False):
    moves = []
    piece = board.board[r][c]

    if piece not in ('N', 'n'):
        return moves

    is_white_knight = piece == 'N'

    for dr, dc in KNIGHT_DELTAS:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < 8 and 0 <= nc < 8:
            target = board.board[nr][nc]

            if target == EMPTY:
                if not captures_only:
                    moves.append((r, c, nr, nc))
            elif is_white_knight and board.is_black(target):
                moves.append((r, c, nr, nc))
            elif not is_white_knight and board.is_white(target):
                moves.append((r, c, nr, nc))

    return moves


def _generate_sliding_moves(board, r, c, piece_type, captures_only=False):
    moves = []
    piece = board.board[r][c]

    if piece not in (piece_type, piece_type.lower()):
        return moves

    is_white_piece = piece == piece_type

    for dr, dc in SLIDING_RAYS[piece_type]:
        nr = r + dr
        nc = c + dc

        while 0 <= nr < 8 and 0 <= nc < 8:
            target = board.board[nr][nc]

            if target == EMPTY:
                if not captures_only:
                    moves.append((r, c, nr, nc))
            elif is_white_piece and board.is_black(target):
                moves.append((r, c, nr, nc))
                break
            elif not is_white_piece and board.is_white(target):
                moves.append((r, c, nr, nc))
                break
            else:
                break

            nr += dr
            nc += dc

    return moves


def generate_bishop_moves(board, r, c, captures_only=False):
    return _generate_sliding_moves(board, r, c, 'B', captures_only)


def generate_rook_moves(board, r, c, captures_only=False):
    return _generate_sliding_moves(board, r, c, 'R', captures_only)


def generate_queen_moves(board, r, c, captures_only=False):
    return _generate_sliding_moves(board, r, c, 'Q', captures_only)


def generate_king_moves(board, r, c, captures_only=False):
    moves = []
    piece = board.board[r][c]

    if piece not in ('K', 'k'):
        return moves

    is_white_king = piece == 'K'
    enemy = BLACK if is_white_king else WHITE

    for dr, dc in KING_DIRECTIONS:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < 8 and 0 <= nc < 8:
            target = board.board[nr][nc]

            if target == EMPTY:
                if captures_only:
                    continue
            elif is_white_king and board.is_black(target):
                pass
            elif not is_white_king and board.is_white(target):
                pass
            else:
                continue

            if not is_square_attacked(board, nr, nc, enemy):
                moves.append((r, c, nr, nc))

    if not captures_only and piece == 'K':
        moves.extend(generate_castling_moves_w(board, r, c))
    elif not captures_only and piece == 'k':
        moves.extend(generate_castling_moves_b(board, r, c))

    return moves


def generate_castling_moves_w(board, r, c):
    moves = []
    piece = board.board[r][c]

    if piece == 'K':
        if board.white_king_moved:
            return moves

        opponent = BLACK

        if not board.white_rook_moved['h'] and board.board[7][7] == 'R':
            if board.board[7][5] == EMPTY and board.board[7][6] == EMPTY:
                if not is_square_attacked(board, 7, 4, opponent) and \
                        not is_square_attacked(board, 7, 5, opponent) and \
                        not is_square_attacked(board, 7, 6, opponent):
                    moves.append((7, 4, 7, 6, 'castle'))

        if not board.white_rook_moved['a'] and board.board[7][0] == 'R':
            if board.board[7][1] == EMPTY and board.board[7][2] == EMPTY and board.board[7][3] == EMPTY:
                if not is_square_attacked(board, 7, 4, opponent) and \
                        not is_square_attacked(board, 7, 3, opponent) and \
                        not is_square_attacked(board, 7, 2, opponent):
                    moves.append((7, 4, 7, 2, 'castle'))

    return moves


def generate_castling_moves_b(board, r, c):
    moves = []
    piece = board.board[r][c]

    if piece == 'k':
        if board.black_king_moved:
            return moves

        opponent = WHITE

        if not board.black_rook_moved['h'] and board.board[0][7] == 'r':
            if board.board[0][5] == EMPTY and board.board[0][6] == EMPTY:
                if not is_square_attacked(board, 0, 4, opponent) and \
                   not is_square_attacked(board, 0, 5, opponent) and \
                   not is_square_attacked(board, 0, 6, opponent):
                    moves.append((0, 4, 0, 6, 'castle'))

        if not board.black_rook_moved['a'] and board.board[0][0] == 'r':
            if board.board[0][1] == EMPTY and board.board[0][2] == EMPTY and board.board[0][3] == EMPTY:
                if not is_square_attacked(board, 0, 4, opponent) and \
                    not is_square_attacked(board, 0, 3, opponent) and \
                    not is_square_attacked(board, 0, 2, opponent):
                    moves.append((0, 4, 0, 2, 'castle'))

    return moves


def generate_piece_moves(board, r, c, captures_only=False):
    piece = board.board[r][c]

    if piece == EMPTY:
        return []

    generator_name = MOVE_GENERATORS.get(piece.upper())
    if generator_name is None:
        return []

    return globals()[generator_name](board, r, c, captures_only)


def generate_all_pseudo_moves(board, color, captures_only=False):
    moves = []

    for r in range(8):
        for c in range(8):
            piece = board.board[r][c]

            if piece == EMPTY:
                continue

            if color == WHITE and board.is_white(piece):
                moves += generate_piece_moves(board, r, c, captures_only)
            elif color == BLACK and board.is_black(piece):
                moves += generate_piece_moves(board, r, c, captures_only)

    return moves


def generate_legal_moves(board, r, c):
    legal_moves = []
    piece = board.board[r][c]
    color = WHITE if board.is_white(piece) else BLACK
    pseudo_moves = generate_piece_moves(board, r, c)

    for move in pseudo_moves:
        board.make_move(move)

        if not is_in_check(board, color):
            legal_moves.append(move)

        board.undo_move()

    return legal_moves


def generate_all_legal_moves(board, color):
    legal = []

    for r in range(8):
        for c in range(8):
            piece = board.board[r][c]

            if piece == EMPTY:
                continue

            if color == WHITE and board.is_white(piece):
                legal += generate_legal_moves(board, r, c)
            elif color == BLACK and board.is_black(piece):
                legal += generate_legal_moves(board, r, c)

    return legal


def has_legal_moves(board, color):
    for r in range(8):
        for c in range(8):
            piece = board.board[r][c]

            if piece == EMPTY:
                continue

            if color == WHITE and not board.is_white(piece):
                continue
            if color == BLACK and not board.is_black(piece):
                continue

            for move in generate_piece_moves(board, r, c):
                board.make_move(move)
                legal = not is_in_check(board, color)
                board.undo_move()

                if legal:
                    return True

    return False


def is_square_attacked(board, r, c, by_color):
    white = by_color == WHITE
    knight = 'N' if white else 'n'
    king = 'K' if white else 'k'

    for dr, dc in KNIGHT_DELTAS:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < 8 and 0 <= nc < 8 and board.board[nr][nc] == knight:
            return True

    for dr, dc in KING_DIRECTIONS:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < 8 and 0 <= nc < 8 and board.board[nr][nc] == king:
            return True

    pawn = 'P' if white else 'p'
    pawn_row = r + 1 if white else r - 1
    if 0 <= pawn_row < 8:
        for dc in (-1, 1):
            nc = c + dc
            if 0 <= nc < 8 and board.board[pawn_row][nc] == pawn:
                return True

    for piece_type, rays in SLIDING_RAYS.items():
        sliding_piece = piece_type if white else piece_type.lower()
        for dr, dc in rays:
            nr = r + dr
            nc = c + dc

            while 0 <= nr < 8 and 0 <= nc < 8:
                target = board.board[nr][nc]

                if target == sliding_piece:
                    return True
                if target != EMPTY:
                    break

                nr += dr
                nc += dc

    return False


def find_king(board, color):
    return board.white_king_pos if color == WHITE else board.black_king_pos


def is_in_check(board, color):
    king_pos = find_king(board, color)

    if not king_pos:
        return False

    opponent = BLACK if color == WHITE else WHITE
    kr, kc = king_pos
    return is_square_attacked(board, kr, kc, opponent)


def is_checkmate(board, color):
    return is_in_check(board, color) and not has_legal_moves(board, color)


def is_stalemate(board, color):
    return not is_in_check(board, color) and not has_legal_moves(board, color)
