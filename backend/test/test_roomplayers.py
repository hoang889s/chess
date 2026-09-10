import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from oop_data.room_players import Room_players
def run_test():
    room_players = Room_players(1,1,2,"white",1634567890,1634567890,"active")
    room_players.test_room_players_print()
    print(f"giá trị trả về:+{room_players.return_value_room_players()}")

if __name__ == "__main__":
    run_test()