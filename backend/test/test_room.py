import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from oop_data.room import Room
def run_test():
    room = Room(1,"ABCD",1,1,"active",False,1634567890,1634567890)
    room.test_room_print()
    print(f"giá trị trả về:+{room.return_value_room()}")

if __name__ == "__main__":
    run_test()
