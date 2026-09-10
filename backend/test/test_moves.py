import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from oop_data.moves import Move
def run_test():
    move = Move(1,1,2,1,"e4",None,"e4","rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",1634567890)
    move.test_move_print()
    print(f"giá trị trả về:+{move.return_value_move()}")

if __name__ == "__main__":
    run_test()