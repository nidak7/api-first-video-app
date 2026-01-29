from flask_jwt_extended import create_access_token, decode_token, get_jwt_identity
from datetime import timedelta

def get_current_user():
    return get_jwt_identity()


def generate_jwt(identity):
    """
    Generate a JWT token for a given identity (e.g., user email)
    Token expires in 1 day
    """
    return create_access_token(identity=identity, expires_delta=timedelta(days=1))


def decode_jwt(token):
    """
    Decode a JWT token and return the identity
    """
    try:
        decoded = decode_token(token)
        return decoded['sub']
    except Exception:
        return None
