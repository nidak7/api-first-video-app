from datetime import datetime
from utils.security import hash_password


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = hash_password(password)
        self.created_at = datetime.utcnow()


    def save(self):
        from extensions import db
        return db.users.insert_one({
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash,
            "created_at": self.created_at
        })

    @staticmethod
    def find_by_email(email):
        from extensions import db
        return db.users.find_one({"email": email})
