import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.board import Board
from core.minimax import Minimax
from core.constants import WHITE, BLACK

def parse_uci_move(uci_str: str) -> tuple:
    """Chuyển đổi chuỗi nước đi chuẩn UCI (ví dụ 'e2e4') sang định dạng tuple của Board."""
    if len(uci_str) < 4:
        raise ValueError("Định dạng nước đi UCI không hợp lệ.")
    
    fc = ord(uci_str[0]) - ord('a')
    fr = 8 - int(uci_str[1])
    tc = ord(uci_str[2]) - ord('a')
    tr = 8 - int(uci_str[3])
    
    # Trường hợp phong cấp (ví dụ 'e7e8q')
    if len(uci_str) == 5:
        promo = uci_str[4].upper()
        return (fr, fc, tr, tc, promo)
        
    return (fr, fc, tr, tc)

def format_to_uci(move: tuple) -> str:
    """Chuyển đổi tuple nước đi của Board sang chuỗi UCI."""
    fr, fc, tr, tc = move[0], move[1], move[2], move[3]
    from_sq = chr(fc + ord('a')) + str(8 - fr)
    to_sq = chr(tc + ord('a')) + str(8 - tr)
    
    promo = ""
    # Nếu có nước đi phong cấp
    if len(move) == 5 and move[4] not in ("castle", "en_passant", None):
        promo = str(move[4]).lower()
        
    return from_sq + to_sq + promo

def run_simulation():
    # 1. Khởi tạo bàn cờ và AI
    print("=== KHỞI TẠO TRẬN ĐẤU ===")
    board = Board()
    ai = Minimax(depth=4)
    
    print("Bàn cờ ban đầu:")
    board.print_board()
    
    while True:
        current_turn = board.turn
        
        # Kiểm tra kết thúc trận đấu (Checkmate / Stalemate)
        if not board.has_legal_moves(current_turn):
            if board.is_in_check(current_turn):
                winner = "AI (Quân Đen)" if current_turn == WHITE else "Người chơi (Quân Trắng)"
                print(f"\n=== TRẬN ĐẤU KẾT THÚC: CHIẾU BÍ (CHECKMATE)! {winner} CHIẾN THẮNG ===")
            else:
                print("\n=== TRẬN ĐẤU KẾT THÚC: HÒA CỜ (STALEMATE) ===")
            break

        if current_turn == WHITE:
            # Lượt của Người chơi
            print(f"\n--- Lượt của Người chơi (Quân Trắng) ---")
            matched_move = None
            human_input = ""
            while True:
                human_input = input("Nhập nước đi của bạn (ví dụ: e2e4, hoặc 'quit' để thoát): ").strip().lower()
                if human_input in ('quit', 'exit', 'q'):
                    print("Người chơi đã xin thua / thoát trận đấu.")
                    return
                
                try:
                    player_move = parse_uci_move(human_input)
                    legal_moves = board.generate_all_legal_moves(board.turn)
                    
                    # Kiểm tra nước đi hợp lệ
                    for m in legal_moves:
                        if m[:4] == player_move[:4]:
                            matched_move = m
                            break
                            
                    if matched_move:
                        break
                    else:
                        print(f"Lỗi: Nước đi {human_input} không phải là nước đi hợp lệ! Vui lòng thử lại.")
                except Exception as e:
                    print(f"Lỗi: Định dạng nước đi không hợp lệ ({e}). Vui lòng nhập lại (ví dụ: e2e4).")
            
            print(f"Người chơi đã chọn nước đi: {human_input}")
            try:
                board.make_move(matched_move)
                print("Đã thực hiện nước đi của Người chơi thành công.")
                board.print_board()
            except Exception as e:
                print(f"Lỗi khi xử lý nước đi của người chơi: {e}")
                return
        else:
            # Lượt của AI
            print(f"\n--- Lượt của AI (Quân Đen) ---")
            print("AI đang suy nghĩ nước đi đáp trả...")
            
            ai.init_score(board)
            ai_move = ai.find_best_move(board, board.turn)
            
            if ai_move:
                ai_move_uci = format_to_uci(ai_move)
                print(f"AI quyết định đi nước: {ai_move_uci}")
                board.make_move(ai_move)
                board.print_board()
            else:
                # Trường hợp không tìm được nước đi (thường không xảy ra vì has_legal_moves đã check trước đó)
                if board.is_in_check(board.turn):
                    print("Trò chơi kết thúc: AI bị Chiếu bí (Checkmate)!")
                else:
                    print("Trò chơi kết thúc: Hòa cờ (Stalemate)!")
                break

if __name__ == "__main__":
    run_simulation()