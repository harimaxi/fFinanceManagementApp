import sqlite3

def get_db_connection():
    conn = sqlite3.connect('finance_manager.db')
    conn.row_factory = sqlite3.Row
    return conn

def initialize_db():
    with get_db_connection() as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        ''')
        conn.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            amount REAL,
            type TEXT,
            date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        ''')



#----------------------------------------------------------------------------

import shutil
import os

def backup_db():
    if os.path.exists('finance_manager.db'):
        shutil.copy('finance_manager.db', 'finance_manager_backup.db')
        print("Backup successful.")
    else:
        print("Database does not exist.")

def restore_db():
    if os.path.exists('finance_manager_backup.db'):
        shutil.copy('finance_manager_backup.db', 'finance_manager.db')
        print("Restore successful.")
    else:
        print("Backup does not exist.")
