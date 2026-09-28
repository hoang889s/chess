from flask_jwt_extended import get_jwt
revoked_tokens = set()
def revoked_token():
    """dua token hien tai vao block list"""
    jwt_data = get_jwt()
    jti  =  jwt_data["jti"]
    revoked_tokens.add(jti)

def is_token_revokes(jwt_payload):
    """kiem tra co nam trong blocklist hay khong"""
    jti = jwt_payload["jti"]
    return jti in revoked_tokens

