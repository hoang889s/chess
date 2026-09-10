import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from oop_data.user import User
def run_test():
    user = User(1,"hoang","123456","Hoang145236@gmail.com",5,"user",True,50,50,1634567890,1630)
    user.test_user_print()
    print(f"giá trị trả về:+{user.return_value_user()}")

if __name__ == "__main__":
    run_test()

