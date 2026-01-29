from flask import Blueprint, request, jsonify
from models.user import User
from utils.security import verify_password
from utils.jwt_utils import get_current_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/signup', methods=['POST'])
def signup():
    """
    Register a new user
    Expects JSON: { "name": "", "email": "", "password": "" }
    """
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "All fields are required"}), 400

    existing_user = User.find_by_email(data["email"])
    if existing_user:
        return jsonify({"error": "Email already registered"}), 409

    new_user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"]
    )
    new_user.save()

    token = create_access_token(identity=data["email"])

    return jsonify({
        "message": "User created successfully",
        "token": token
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password required"}), 400

    user = User.find_by_email(data["email"])
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if not verify_password(data["password"], user["password_hash"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=user["email"])

    return jsonify({
        "token": token
    }), 200

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    current_user_email = get_jwt_identity()
    user = User.find_by_email(current_user_email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "name": user["name"],
        "email": user["email"],
        "created_at": user["created_at"]
    }), 200