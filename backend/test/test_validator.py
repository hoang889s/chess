import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.validator import (validate_username, validate_email, validate_password)
def run_test():
    print(validate_username("hoang"))
    print(validate_email("hahaa@gmail.com"))
    print(validate_password("password123"))
if __name__ == "__main__":
    run_test()