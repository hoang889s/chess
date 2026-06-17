from core.constants import WHITE, BLACK, EMPTY, PIECE_SCORES, MVV_LVA_PRECOMPUTED


def _piece_score(piece: str, r: int, c: int) -> int:
    if piece == EMPTY:
        return 0
    return PIECE_SCORES[piece][r][c]


class Minimax:
    def __init__(self, depth):
        self.depth = depth
        self.transposition_table: dict = {}
        self.TT_MAX_SIZE = 1_000_000
        self.killer_moves = [[None, None] for _ in range(64)]
        self.history_table: dict = {}
        self.node_searched = 0
        self.tt_hits = 0
        self._inc_score: int = 0
        self._score_stack: list = []

    def init_score(self, board) -> None:
        score = 0
        for r in range(8):
            for c in range(8):
                piece = board.board[r][c]
                if piece != EMPTY:
                    score += _piece_score(piece, r, c)

        self._inc_score = score
        self._score_stack.clear()

    def push_move(self, board, move: tuple) -> None:
        fr, fc, tr, tc = move[0], move[1], move[2], move[3]
        move_type = move[4] if len(move) == 5 else None
        piece = board.board[fr][fc]
        captured = board.board[tr][tc]
        delta = self._calculate_move_delta(board, piece, captured, fr, fc, tr, tc, move_type)

        self._score_stack.append(self._inc_score)
        self._inc_score += delta
        board.make_move(move)

    def pop_move(self, board) -> None:
        board.undo_move()
        self._inc_score = self._score_stack.pop()

    def evaluate(self, board) -> int:
        return self._inc_score

    def _calculate_move_delta(self, board, piece, captured, fr, fc, tr, tc, move_type) -> int:
        delta = 0
        delta -= _piece_score(piece, fr, fc)

        if captured != EMPTY:
            delta -= _piece_score(captured, tr, tc)

        landing = self._get_landing_piece(piece, move_type)
        delta += _piece_score(landing, tr, tc)

        if move_type == "castle":
            delta += self._calculate_castle_delta(piece, tc)

        return delta

    def _get_landing_piece(self, piece, move_type):
        if move_type and move_type.startswith("promotion"):
            promo_char = move_type.split("_")[1]
            return promo_char.upper() if piece.isupper() else promo_char.lower()
        if move_type and move_type in ('Q', 'R', 'B', 'N'):
            return move_type.upper() if piece.isupper() else move_type.lower()

        return piece

    def _calculate_castle_delta(self, piece, tc) -> int:
        if piece == 'K':
            if tc == 6:
                return -_piece_score('R', 7, 7) + _piece_score('R', 7, 5)
            return -_piece_score('R', 7, 0) + _piece_score('R', 7, 3)

        if piece == 'k':
            if tc == 6:
                return -_piece_score('r', 0, 7) + _piece_score('r', 0, 5)
            return -_piece_score('r', 0, 0) + _piece_score('r', 0, 3)

        return 0

    def _move_score(self, move, board, depth: int, tt_move=None) -> int:
        fr, fc, tr, tc = move[0], move[1], move[2], move[3]
        target = board.board[tr][tc]
        attacker = board.board[fr][fc]

        if move == tt_move:
            return 30_000
        if target != EMPTY:
            return 10_000 + MVV_LVA_PRECOMPUTED.get((attacker.upper(), target.upper()), 0)
        if move == self.killer_moves[depth][0]:
            return 9_000
        if move == self.killer_moves[depth][1]:
            return 8_000

        return self.history_table.get((move[0], move[1], move[2], move[3]), 0)

    def _order_moves(self, moves, board, depth: int, tt_move=None):
        return sorted(moves, key=lambda move: self._move_score(move, board, depth, tt_move), reverse=True)

    def _update_killer(self, move, depth: int) -> None:
        if move != self.killer_moves[depth][0]:
            self.killer_moves[depth][1] = self.killer_moves[depth][0]
            self.killer_moves[depth][0] = move

    def _update_history(self, move, depth: int) -> None:
        key = (move[0], move[1], move[2], move[3])
        self.history_table[key] = self.history_table.get(key, 0) + depth * depth

    def quiescence(self, board, alpha, beta, maximizing, q_depth: int = 4):
        stand_pat = self.evaluate(board)

        if maximizing:
            return self._quiescence_max(board, alpha, beta, stand_pat, q_depth)

        return self._quiescence_min(board, alpha, beta, stand_pat, q_depth)

    def _quiescence_max(self, board, alpha, beta, stand_pat, q_depth):
        if stand_pat >= beta:
            return beta

        alpha = max(alpha, stand_pat)
        if q_depth == 0:
            return alpha

        captures = board.generate_all_pseudo_moves(WHITE, captures_only=True)

        for move in self._order_moves(captures, board, 0):
            self.push_move(board, move)
            score = self.quiescence(board, alpha, beta, False, q_depth - 1)
            self.pop_move(board)

            if score >= beta:
                return beta

            alpha = max(alpha, score)

        return alpha

    def _quiescence_min(self, board, alpha, beta, stand_pat, q_depth):
        if stand_pat <= alpha:
            return alpha

        beta = min(beta, stand_pat)
        if q_depth == 0:
            return beta

        captures = board.generate_all_pseudo_moves(BLACK, captures_only=True)

        for move in self._order_moves(captures, board, 0):
            self.push_move(board, move)
            score = self.quiescence(board, alpha, beta, True, q_depth - 1)
            self.pop_move(board)

            if score <= alpha:
                return alpha

            beta = min(beta, score)

        return beta

    def minimax(self, board, depth: int, alpha, beta, maximizing) -> int:
        self.node_searched += 1
        alpha_orig = alpha
        board_hash = board.get_hash() if hasattr(board, 'get_hash') else None
        alpha, beta, tt_move, tt_score = self._lookup_transposition_table(board_hash, depth, alpha, beta)

        if tt_score is not None:
            return tt_score

        current_color = WHITE if maximizing else BLACK
        terminal_score = self._check_terminal_nodes(board, current_color, maximizing)

        if terminal_score is not None:
            return terminal_score

        if depth == 0:
            return self.quiescence(board, alpha, beta, maximizing)

        all_moves = self._order_moves(board.generate_all_pseudo_moves(current_color), board, depth, tt_move)
        null_move_score = self._null_move_pruning(board, depth, alpha, beta, maximizing, current_color, all_moves)

        if null_move_score is not None:
            return null_move_score

        best_score, best_move_local, alpha, beta = self._search_moves(
            board, depth, alpha, beta, maximizing, all_moves
        )
        self._save_transposition_table(board_hash, depth, alpha_orig, beta, best_score, best_move_local)

        return best_score

    def _lookup_transposition_table(self, board_hash, depth, alpha, beta):
        tt_move = None

        if board_hash and board_hash in self.transposition_table:
            tt_depth, tt_flag, tt_score, tt_best = self.transposition_table[board_hash]
            tt_move = tt_best

            if tt_depth >= depth:
                self.tt_hits += 1

                if tt_flag == 'EXACT':
                    return alpha, beta, tt_move, tt_score
                if tt_flag == 'LOWER':
                    alpha = max(alpha, tt_score)
                if tt_flag == 'UPPER':
                    beta = min(beta, tt_score)
                if alpha >= beta:
                    return alpha, beta, tt_move, tt_score

        return alpha, beta, tt_move, None

    def _check_terminal_nodes(self, board, current_color, maximizing):
        if not board.has_legal_moves(current_color):
            if board.is_in_check(current_color):
                return -99999 if maximizing else 99999
            return 0

        return None

    def _null_move_pruning(self, board, depth, alpha, beta, maximizing, current_color, all_moves):
        if depth >= 3 and hasattr(board, 'make_null_move') and not board.is_in_check(current_color) and all_moves:
            board.make_null_move()
            null_score = self.minimax(board, depth - 3, alpha, beta, not maximizing)
            board.undo_null_move()

            if maximizing and null_score >= beta:
                return beta
            if not maximizing and null_score <= alpha:
                return alpha

        return None

    def _should_lmr(self, index, depth, is_capture, move) -> bool:
        return index >= 4 and depth >= 3 and not is_capture and move not in self.killer_moves[depth]

    def _search_moves(self, board, depth, alpha, beta, maximizing, all_moves):
        best_score = -float('inf') if maximizing else float('inf')
        best_move_local = None

        for index, move in enumerate(all_moves):
            is_capture = self._is_capture(board, move)

            if self._should_lmr(index, depth, is_capture, move):
                self.push_move(board, move)
                lmr_score = self.minimax(board, depth - 2, alpha, beta, not maximizing)
                self.pop_move(board)

                if (maximizing and lmr_score <= alpha) or (not maximizing and lmr_score >= beta):
                    continue

            self.push_move(board, move)
            eval_score = self.minimax(board, depth - 1, alpha, beta, not maximizing)
            self.pop_move(board)

            if maximizing:
                if eval_score > best_score:
                    best_score = eval_score
                    best_move_local = move
                if eval_score > alpha:
                    alpha = eval_score
                if alpha >= beta:
                    if not is_capture:
                        self._update_killer(move, depth)
                        self._update_history(move, depth)
                    break
            else:
                if eval_score < best_score:
                    best_score = eval_score
                    best_move_local = move
                if eval_score < beta:
                    beta = eval_score
                if beta <= alpha:
                    if not is_capture:
                        self._update_killer(move, depth)
                        self._update_history(move, depth)
                    break

        return best_score, best_move_local, alpha, beta

    def _save_transposition_table(self, board_hash, depth, alpha_orig, beta, best_score, best_move) -> None:
        if board_hash and len(self.transposition_table) < self.TT_MAX_SIZE:
            if best_score <= alpha_orig:
                flag = 'UPPER'
            elif best_score >= beta:
                flag = 'LOWER'
            else:
                flag = 'EXACT'

            self.transposition_table[board_hash] = (depth, flag, best_score, best_move)

    def _is_capture(self, board, move) -> bool:
        return board.board[move[2]][move[3]] != EMPTY

    def find_best_move(self, board, color):
        self._reset_search_stats()
        maximizing = color == WHITE
        best_move = None

        for current_depth in range(1, self.depth + 1):
            alpha = -float('inf')
            beta = float('inf')
            moves = board.generate_all_legal_moves(color)
            moves = self._order_root_moves(moves, best_move)
            depth_best_move = self._search_root_depth(board, current_depth, moves, alpha, beta, maximizing)

            if depth_best_move:
                best_move = depth_best_move

        return best_move

    def _reset_search_stats(self) -> None:
        self.node_searched = 0
        self.tt_hits = 0
        self.killer_moves = [[None, None] for _ in range(64)]

    def _order_root_moves(self, moves, best_move):
        if best_move and best_move in moves:
            moves.remove(best_move)
            moves.insert(0, best_move)

        return moves

    def _search_root_depth(self, board, current_depth, moves, alpha, beta, maximizing):
        depth_best_move = None
        depth_best_value = -float('inf') if maximizing else float('inf')

        for move in moves:
            self.push_move(board, move)
            value = self.minimax(board, current_depth - 1, alpha, beta, not maximizing)
            self.pop_move(board)

            if maximizing:
                if value > depth_best_value:
                    depth_best_value = value
                    depth_best_move = move
                alpha = max(alpha, value)
            else:
                if value < depth_best_value:
                    depth_best_value = value
                    depth_best_move = move
                beta = min(beta, value)

        return depth_best_move
