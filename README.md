# fFinanceManagementApp
 A command-line application that helps users manage their personal finances by tracking income, expenses, and generating financial reports.

# Personal Finance Management Application

# Personal Finance Management Application

## Overview
This command-line application helps users manage their personal finances by tracking income, expenses, and generating financial reports.

## Features
1. User Registration and Authentication
2. Income and Expense Tracking
3. Financial Reports
4. Budgeting
5. Data Persistence

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd finance_manager
    ```
3. Install dependencies:
    ```bash
    pip install sqlite3
    ```

## Usage
1. Run the application:
    ```bash
    python app.py
    ```
2. Follow the prompts to register, log in, and manage finances.

## Commands
- **Register**: Create a new user account.
- **Login**: Authenticate an existing user.
- **Add Transaction**: Record an income or expense.
- **Update Transaction**: Modify an existing transaction.
- **Delete Transaction**: Remove a transaction.
- **Generate Report**: View monthly or yearly financial reports.
- **Set Budget**: Define monthly budgets for different categories.
- **Check Budget**: Monitor spending against set budgets.

## Backup and Restore
- **Backup Data**: `python db.py backup_db`
- **Restore Data**: `python db.py restore_db`

## Testing
Run unit tests to verify functionality:
```bash
python -m unittest discover tests/