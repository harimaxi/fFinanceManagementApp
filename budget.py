import db
def set_budget(user_id, category, amount):
    with db.get_db_connection() as conn:
        conn.execute('INSERT INTO budgets (user_id, category, amount) VALUES (?, ?, ?)',
                     (user_id, category, amount))
        conn.commit()
        print("Budget set.")

def check_budget(user_id):
    with db.get_db_connection() as conn:
        budgets = conn.execute('SELECT * FROM budgets WHERE user_id = ?', (user_id,)).fetchall()
        transactions = conn.execute('SELECT category, SUM(amount) AS spent FROM transactions WHERE user_id = ? GROUP BY category',
                                    (user_id,)).fetchall()

        budget_dict = {row['category']: row['amount'] for row in budgets}
        spent_dict = {row['category']: row['spent'] for row in transactions}

        for category, amount in budget_dict.items():
            spent = spent_dict.get(category, 0)
            if spent > amount:
                print(f"Warning: Budget exceeded for {category}. Spent: {spent}, Budget: {amount}")
