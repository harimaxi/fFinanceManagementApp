import hashlib
import db
import sqlite3

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    with db.get_db_connection() as conn:
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                         (username, hash_password(password)))
            conn.commit()
            print("Registration successful!")
        except sqlite3.IntegrityError:
            print("Username already exists.")

def authenticate_user(username, password):
    hashed_password = hash_password(password)
    with db.get_db_connection() as conn:
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?',
                            (username, hashed_password)).fetchone()
        return user is not None
