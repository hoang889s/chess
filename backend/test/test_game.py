import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from oop_data.game import Game
def run_test():
    game = Game(1,1,2,"casual",1,"active","pending",1,"start_fen","start_pgn",1634567890,0,1634567890)
    game.test_game_print()
    print(f"giá trị trả về:+{game.return_value_game()}")

if __name__ == "__main__":
    run_test()