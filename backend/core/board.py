from core.constants import WHITE, BLACK, EMPTY
from core import move_generator
from core.zobrist import ZOBRIST_TABLE, ZOBRIST_TURN


class Board:
    def __init__(self):
        self.board = [
             ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
             ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ]
        self.white_king_moved = False
        self.black_king_moved = False
        self.white_rook_moved = {'a': False, 'h': False}
        self.black_rook_moved = {'a': False, 'h': False}
        self.white_king_pos = (7, 4)
        self.black_king_pos = (0, 4)
        self.turn = WHITE
        self.move_history = []
        self.hash_key = self._initial_hash()

    def _initial_hash(self):
        h = 0

        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece != EMPTY:
                    h ^= ZOBRIST_TABLE[piece][r][c]

        if self.turn == BLACK:
            h ^= ZOBRIST_TURN

        return h

    def print_board(self):
        print(" a b c d e f g h")
        for i, row in enumerate(self.board):
            print(f"{8 - i}" + " ".join(row))
        print()

    def get_piece(self, r, c):
        return self.board[r][c]

    def is_white(self, piece):
        return piece.isupper()

    def is_black(self, piece):
        return piece.islower()

    def make_move(self, move):
        if len(move) == 5:
            fr, fc, tr, tc, move_type = move
        else:
            fr, fc, tr, tc = move
            move_type = None

        piece = self.board[fr][fc]
        captured = self.board[tr][tc]
        landing_piece = self._landing_piece(piece, move_type)
        rook_move = self._rook_move_for_castle(piece, tc, move_type)

        self.move_history.append({
            "fr": fr,
            "fc": fc,
            "tr": tr,
            "tc": tc,
            "piece": piece,
            "captured": captured,
            "move_type": move_type,
            "white_king_moved": self.white_king_moved,
            "black_king_moved": self.black_king_moved,
            "white_rook_moved": self.white_rook_moved.copy(),
            "black_rook_moved": self.black_rook_moved.copy(),
            "white_king_pos": self.white_king_pos,
            "black_king_pos": self.black_king_pos,
            "turn": self.turn,
            "hash_key": self.hash_key,
        })

        self.board[fr][fc] = EMPTY

        if move_type == "castle":
            self.board[tr][tc] = piece
            if rook_move:
                rook_from, rook_to = rook_move
                rook_piece = self.board[rook_from[0]][rook_from[1]]
                self.board[rook_from[0]][rook_from[1]] = EMPTY
                self.board[rook_to[0]][rook_to[1]] = rook_piece
        elif move_type and move_type in ('Q', 'R', 'B', 'N'):
            self.board[tr][tc] = landing_piece
        else:
            self.board[tr][tc] = piece

        if piece == 'K':
            self.white_king_moved = True
            self.white_king_pos = (tr, tc)
        elif piece == 'k':
            self.black_king_moved = True
            self.black_king_pos = (tr, tc)

        if piece == 'R':
            if fc == 0:
                self.white_rook_moved['a'] = True
            elif fc == 7:
                self.white_rook_moved['h'] = True
        elif piece == 'r':
            if fc == 0:
                self.black_rook_moved['a'] = True
            elif fc == 7:
                self.black_rook_moved['h'] = True

        if captured == 'R':
            if tr == 7 and tc == 0:
                self.white_rook_moved['a'] = True
            elif tr == 7 and tc == 7:
                self.white_rook_moved['h'] = True

        if captured == 'r':
            if tr == 0 and tc == 0:
                self.black_rook_moved['a'] = True
            elif tr == 0 and tc == 7:
                self.black_rook_moved['h'] = True

        self._update_hash_after_move(piece, landing_piece, captured, fr, fc, tr, tc, rook_move)
        self.turn = BLACK if self.turn == WHITE else WHITE

    def undo_move(self):
        state = self.move_history.pop()
        fr = state["fr"]
        fc = state["fc"]
        tr = state["tr"]
        tc = state["tc"]

        self.board[fr][fc] = state["piece"]
        self.board[tr][tc] = state["captured"]

        if state["move_type"] == "castle":
            if state["piece"] == "K":
                if tc == 6:
                    self.board[7][7] = 'R'
                    self.board[7][5] = EMPTY
                else:
                    self.board[7][0] = 'R'
                    self.board[7][3] = EMPTY
            elif state["piece"] == 'k':
                if tc == 6:
                    self.board[0][7] = 'r'
                    self.board[0][5] = EMPTY
                else:
                    self.board[0][0] = 'r'
                    self.board[0][3] = EMPTY

        self.white_king_moved = state["white_king_moved"]
        self.black_king_moved = state["black_king_moved"]
        self.white_rook_moved = state["white_rook_moved"]
        self.black_rook_moved = state["black_rook_moved"]
        self.white_king_pos = state["white_king_pos"]
        self.black_king_pos = state["black_king_pos"]
        self.turn = state["turn"]
        self.hash_key = state["hash_key"]

    def get_hash(self):
        return self.hash_key

    def make_null_move(self):
        self.move_history.append({
            "fr": None, "fc": None, "tr": None, "tc": None,
            "piece": None, "captured": None,
            "move_type": "null_move",
            "white_king_moved": self.white_king_moved,
            "black_king_moved": self.black_king_moved,
            "white_rook_moved": self.white_rook_moved.copy(),
            "black_rook_moved": self.black_rook_moved.copy(),
            "white_king_pos": self.white_king_pos,
            "black_king_pos": self.black_king_pos,
            "turn": self.turn,
            "hash_key": self.hash_key,
        })
        self.turn = BLACK if self.turn == WHITE else WHITE
        self.hash_key ^= ZOBRIST_TURN

    def undo_null_move(self):
        state = self.move_history.pop()
        self.turn = state["turn"]
        self.white_king_moved = state["white_king_moved"]
        self.black_king_moved = state["black_king_moved"]
        self.white_rook_moved = state["white_rook_moved"]
        self.black_rook_moved = state["black_rook_moved"]
        self.white_king_pos = state["white_king_pos"]
        self.black_king_pos = state["black_king_pos"]
        self.hash_key = state["hash_key"]

    def generate_pawn_moves(self, r, c, captures_only=False):
        return move_generator.generate_pawn_moves(self, r, c, captures_only)

    def generate_knight_moves(self, r, c, captures_only=False):
        return move_generator.generate_knight_moves(self, r, c, captures_only)

    def generate_bishop_moves(self, r, c, captures_only=False):
        return move_generator.generate_bishop_moves(self, r, c, captures_only)

    def generate_rook_moves(self, r, c, captures_only=False):
        return move_generator.generate_rook_moves(self, r, c, captures_only)

    def generate_queen_moves(self, r, c, captures_only=False):
        return move_generator.generate_queen_moves(self, r, c, captures_only)

    def generate_king_moves(self, r, c, captures_only=False):
        return move_generator.generate_king_moves(self, r, c, captures_only)

    def generate_castling_moves_w(self, r, c):
        return move_generator.generate_castling_moves_w(self, r, c)

    def generate_castling_moves_b(self, r, c):
        return move_generator.generate_castling_moves_b(self, r, c)

    def generate_piece_moves(self, r, c, captures_only=False):
        return move_generator.generate_piece_moves(self, r, c, captures_only)

    def generate_all_pseudo_moves(self, color, captures_only=False):
        return move_generator.generate_all_pseudo_moves(self, color, captures_only)

    def generate_legal_moves(self, r, c):
        return move_generator.generate_legal_moves(self, r, c)

    def generate_all_legal_moves(self, color):
        return move_generator.generate_all_legal_moves(self, color)

    def has_legal_moves(self, color):
        return move_generator.has_legal_moves(self, color)

    def is_square_attacked(self, r, c, by_color):
        return move_generator.is_square_attacked(self, r, c, by_color)

    def find_king(self, color):
        return move_generator.find_king(self, color)

    def is_in_check(self, color):
        return move_generator.is_in_check(self, color)

    def is_checkmate(self, color):
        return move_generator.is_checkmate(self, color)

    def is_stalemate(self, color):
        return move_generator.is_stalemate(self, color)

    def _landing_piece(self, piece, move_type):
        if move_type and move_type in ('Q', 'R', 'B', 'N'):
            return move_type.upper() if piece.isupper() else move_type.lower()
        return piece

    def _rook_move_for_castle(self, piece, tc, move_type):
        if move_type != "castle":
            return None

        if piece == 'K':
            return ((7, 7), (7, 5)) if tc == 6 else ((7, 0), (7, 3))
        if piece == 'k':
            return ((0, 7), (0, 5)) if tc == 6 else ((0, 0), (0, 3))

        return None

    def _update_hash_after_move(self, piece, landing_piece, captured, fr, fc, tr, tc, rook_move):
        self.hash_key ^= ZOBRIST_TABLE[piece][fr][fc]

        if captured != EMPTY:
            self.hash_key ^= ZOBRIST_TABLE[captured][tr][tc]

        self.hash_key ^= ZOBRIST_TABLE[landing_piece][tr][tc]

        if rook_move:
            rook_from, rook_to = rook_move
            rook_piece = 'R' if piece == 'K' else 'r'
            self.hash_key ^= ZOBRIST_TABLE[rook_piece][rook_from[0]][rook_from[1]]
            self.hash_key ^= ZOBRIST_TABLE[rook_piece][rook_to[0]][rook_to[1]]

        self.hash_key ^= ZOBRIST_TURN
