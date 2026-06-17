import random

PIECES = ['P', 'N', 'B', 'R', 'Q', 'K', 'p', 'n', 'b', 'r', 'q', 'k']

# Sinh bảng số ngẫu nhiên 64-bit một lần duy nhất khi khởi động
ZOBRIST_TABLE = {
    piece: [[random.getrandbits(64) for _ in range(8)] for _ in range(8)]
    for piece in PIECES
}

ZOBRIST_TURN = random.getrandbits(64)   # XOR vào khi đến lượt đen
