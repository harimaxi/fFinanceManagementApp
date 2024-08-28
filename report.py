import sqlite3
import db


def generate_report(user_id, period='monthly'):
    query = '''
    SELECT strftime('%Y-%m', date) AS month, type, SUM(amount) AS total
    FROM transactions
    WHERE user_id = ?
    GROUP BY month, type
    '''
    if period == 'yearly':
        query = query.replace('%Y-%m', '%Y')

    with db.get_db_connection() as conn:
        report = conn.execute(query, (user_id,)).fetchall()
        return report


def print_report(report):
    for row in report:
        print(f"Month: {row['month']}, Type: {row['type']}, Total: {row['total']}")
