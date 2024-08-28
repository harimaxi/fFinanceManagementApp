import user
import db

def main():
    db.initialize_db()
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user.register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user.authenticate_user(username, password):
                print("Login successful!")
                # Proceed to main application functionality
            else:
                print("Invalid username or password.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()



#---------------------------------------------------------------

import finance

def handle_transactions(user_id):
    while True:
        print("1. Add Transaction")
        print("2. Update Transaction")
        print("3. Delete Transaction")
        print("4. Back")
        choice = input("Choose an option: ")
        if choice == '1':
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            transaction_type = input("Enter type (Income/Expense): ")
            date = input("Enter date (YYYY-MM-DD): ")
            finance.add_transaction(user_id, category, amount, transaction_type, date)
        elif choice == '2':
            transaction_id = int(input("Enter transaction ID: "))
            category = input("Enter new category: ")
            amount = float(input("Enter new amount: "))
            transaction_type = input("Enter new type (Income/Expense): ")
            date = input("Enter new date (YYYY-MM-DD): ")
            finance.update_transaction(transaction_id, category, amount, transaction_type, date)
        elif choice == '3':
            transaction_id = int(input("Enter transaction ID: "))
            finance.delete_transaction(transaction_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")


#-------------------------------------------------------------------------

import report

def handle_reports(user_id):
    while True:
        print("1. Monthly Report")
        print("2. Yearly Report")
        print("3. Back")
        choice = input("Choose an option: ")
        if choice == '1':
            report_data = report.generate_report(user_id, 'monthly')
            report.print_report(report_data)
        elif choice == '2':
            report_data = report.generate_report(user_id, 'yearly')
            report.print_report(report_data)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")


#----------------------------------------------------------------------------------


import budget

def handle_budget(user_id):
    while True:
        print("1. Set Budget")
        print("2. Check Budget")
        print("3. Back")
        choice = input("Choose an option: ")
        if choice == '1':
            category = input("Enter category: ")
            amount = float(input("Enter budget amount: "))
            budget.set_budget(user_id, category, amount)
        elif choice == '2':
            budget.check_budget(user_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

