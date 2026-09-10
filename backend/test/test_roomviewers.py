import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from oop_data.room_viewers import Room_viewers
def run_test():
    room_viewers = Room_viewers(1,1,2,1634567890,1634567890)
    room_viewers.test_room_viewers_print()
    print(f"giá trị trả về:+{room_viewers.return_value_room_viewers()}")

if __name__ == "__main__":
    run_test()