import unittest
import finance
import db

class TestFinanceFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db.initialize_db()
        cls.user_id = 1  # Assume a user with ID 1 exists

    def test_add_transaction(self):
        finance.add_transaction(self.user_id, "Food", 50.0, "Expense", "2024-08-23")
        with db.get_db_connection() as conn:
            transaction = conn.execute('SELECT * FROM transactions WHERE user_id = ? AND category = ?', (self.user_id, "Food")).fetchone()
            self.assertIsNotNone(transaction)

    def test_update_transaction(self):
        finance.add_transaction(self.user_id, "Food", 50.0, "Expense", "2024-08-23")
        with db.get_db_connection() as conn:
            transaction_id = conn.execute('SELECT id FROM transactions WHERE user_id = ? AND category = ?', (self.user_id, "Food")).fetchone()[0]
        finance.update_transaction(transaction_id, "Groceries", 60.0, "Expense", "2024-08-24")
        with db.get_db_connection() as conn:
            updated_transaction = conn.execute('SELECT * FROM transactions WHERE id = ?', (transaction_id,)).fetchone()
            self.assertEqual(updated_transaction['category'], "Groceries")
            self.assertEqual(updated_transaction['amount'], 60.0)

    def test_delete_transaction(self):
        finance.add_transaction(self.user_id, "Food", 50.0, "Expense", "2024-08-23")
        with db.get_db_connection() as conn:
            transaction_id = conn.execute('SELECT id FROM transactions WHERE user_id = ? AND category = ?', (self.user_id, "Food")).fetchone()[0]
        finance.delete_transaction(transaction_id)
        with db.get_db_connection() as conn:
            transaction = conn.execute('SELECT * FROM transactions WHERE id = ?', (transaction_id,)).fetchone()
            self.assertIsNone(transaction)

if __name__ == '__main__':
    unittest.main()
