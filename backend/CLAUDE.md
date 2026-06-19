# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

This is a small Python chess engine prototype. The repository currently contains only a `core` package with three modules:

- `core/constants.py` — piece values, piece-square tables, move-ordering bonuses, and color/empty-square constants.
- `core/board.py` — board representation, move generation, legality checks, castling, promotion, undo/redo state, Zobrist hashing, and attack detection.
- `core/minimax.py` — AI search over generated legal moves using alpha-beta minimax, quiescence search, move ordering, killer/history heuristics, late move reductions, null-move pruning, and a transposition table.

The backend/engine code is Python-only. The frontend is a separate React JavaScript application under `frontend/chess_ui`.

There is no README, test suite, lint config, formatter config, or executable entrypoint in the repository.

## Frontend overview

The frontend app lives in `frontend/chess_ui` and uses:

- React 19 with JavaScript (`.jsx`), not TypeScript.
- Vite for development, build, preview, and React plugin setup.
- ESLint with the React hooks and React Refresh plugins.
- `src/main.jsx` as the React entrypoint.
- `src/App.jsx` as the root component.
- Public assets in `frontend/chess_ui/public`.

When changing frontend code, work from `frontend/chess_ui` and keep changes consistent with plain JavaScript React conventions. Do not introduce TypeScript unless the project is explicitly migrated.

## Common commands

Because there is no package metadata or scripts, use direct Python commands from the repository root.

```bash
# Syntax-check all Python files
python -m compileall core

# Run a quick import sanity check
python - <<'PY'
from core.board import Board
from core.minimax import Minimax

b = Board()
print(len(b.generate_all_legal_moves(b.turn)))

ai = Minimax(depth=2)
print(ai.find_best_move(b, b.turn))
PY
```

From `frontend/chess_ui`, use the React/Vite scripts:

```bash
# Start the Vite dev server
npm run dev

# Build the React app for production
npm run build

# Lint the frontend
npm run lint

# Preview the production build locally
npm run preview
```

There is currently no configured way to run a single test because no tests exist. If tests are added later, prefer the project’s test runner once one is configured; otherwise use `python -m pytest path/to/test_file.py::test_name` for pytest-style tests.

## Architecture notes

`Board` is the source of truth for the chess position. It stores the board as an 8x8 list with uppercase pieces for White, lowercase pieces for Black, and `EMPTY` (`"."`) for vacant squares. Most move tuples are `(from_row, from_col, to_row, to_col)`; promotions and castling add a fifth `move_type` element.

Move generation is split by piece type in `Board`:

- `generate_pawn_moves`
- `generate_knight_moves`
- `generate_bishop_moves`
- `generate_rook_moves`
- `generate_queen_moves`
- `generate_king_moves`
- `generate_castling_moves_w` / `generate_castling_moves_b`

Legal move generation is currently implemented by applying each pseudo-legal move, checking whether the moving side remains in check, then undoing the move. This means `make_move` / `undo_move` are central to both gameplay and search.

`Minimax` does not copy the board during search. It mutates `Board` with `push_move`, calls `minimax` recursively, then restores state with `pop_move`. When using `Minimax`, call `init_score(board)` before searching so incremental evaluation starts from the current position.

Important `Minimax` methods:

- `find_best_move(board, color)` — iterative deepening entrypoint.
- `minimax(board, depth, alpha, beta, maximizing)` — recursive alpha-beta search.
- `quiescence(board, alpha, beta, maximizing)` — capture-focused extension at leaf nodes.
- `push_move(board, move)` / `pop_move(board)` — keep board state and incremental score in sync.
- `evaluate(board)` — returns the current incremental score rather than recomputing the board.

The Zobrist table is generated randomly at import time. This makes hashes non-deterministic across processes, which is fine for an in-process transposition table but not suitable for persisting positions or comparing hashes between runs.
