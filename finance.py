import db
def add_transaction(user_id, category, amount, transaction_type, date):
    with db.get_db_connection() as conn:
        conn.execute('INSERT INTO transactions (user_id, category, amount, type, date) VALUES (?, ?, ?, ?, ?)',
                     (user_id, category, amount, transaction_type, date))
        conn.commit()
        print("Transaction added.")

def update_transaction(transaction_id, category, amount, transaction_type, date):
    with db.get_db_connection() as conn:
        conn.execute('UPDATE transactions SET category = ?, amount = ?, type = ?, date = ? WHERE id = ?',
                     (category, amount, transaction_type, date, transaction_id))
        conn.commit()
        print("Transaction updated.")

def delete_transaction(transaction_id):
    with db.get_db_connection() as conn:
        conn.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
        conn.commit()
        print("Transaction deleted.")
