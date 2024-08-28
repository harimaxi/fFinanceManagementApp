import unittest
import user
import db

class TestUserFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db.initialize_db()
        cls.test_username = "test_user"
        cls.test_password = "test_password"

    def test_register_user(self):
        user.register_user(self.test_username, self.test_password)
        with db.get_db_connection() as conn:
            user_data = conn.execute('SELECT * FROM users WHERE username = ?', (self.test_username,)).fetchone()
            self.assertIsNotNone(user_data)

    def test_authenticate_user(self):
        user.register_user(self.test_username, self.test_password)
        result = user.authenticate_user(self.test_username, self.test_password)
        self.assertTrue(result)

    def test_failed_authenticate_user(self):
        result = user.authenticate_user(self.test_username, "wrong_password")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()



