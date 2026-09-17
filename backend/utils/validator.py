import re
def validate_username(username:str)->bool:
    """
     kiem tra username voi cac quy tac sau
     + tu 3 den 50 ky tu
     + chi chua cac ky tu chu cai, so, dau gach duoi va dau gach ngang
     + khong khoang trang
    """
    if not isinstance(username, str):
        return False
    username  = username.strip()
    if not 3<= len(username)<=50:
        return False
    pattern = r"^[a-zA-Z)-9]+$"
    return re.fullmatch(pattern, username) is not None
def validate_email(email:str)->bool:
    """
     Kiem tra email voi cac quy tac sau
     + khong duoc rong
     toi da 100 ky tu
     co dang email hop le
     """
    if not isinstance(email, str):
        return False
    email = email.strip()
    if not 1 <= len(email)<=100:
        return False
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.fullmatch(pattern, email) is not None
def validate_password(password:str)->bool:
    """
        Kiem tra password voi cac quy tac sau
        + toi thieu 8 ky tu
        + toi da 128 ky tu
        khong co khoang trang dau hoac cuoi
    """
    if not isinstance(password, str):
        return False
    password = password.strip()
    if not 8 <= len(password) <= 128:
        return False
    if password != password.strip():
        return False
    return True
