"""Simple ATM Simulator (Week 1 Mini Project).
Features: PIN login, check balance, deposit, withdraw.
Uses functions for each operation.
"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
balance = 5000.0


def login():
    """Give the user up to MAX_ATTEMPTS tries to enter the correct PIN."""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin == CORRECT_PIN:
            print("Login successful!\n")
            return True
        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"Incorrect PIN. {remaining} attempt(s) left.")
    print("Too many wrong attempts. Card blocked.")
    return False


def check_balance():
    print(f"Your current balance is: ₹{balance:.2f}")


def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: ₹"))
    except ValueError:
        print("Invalid amount.")
        return
    if amount <= 0:
        print("Deposit amount must be greater than 0.")
        return
    balance += amount
    print(f"₹{amount:.2f} deposited successfully.")
    check_balance()


def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
    except ValueError:
        print("Invalid amount.")
        return
    if amount <= 0:
        print("Withdrawal amount must be greater than 0.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
        check_balance()


def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def main():
    print("=== Welcome to the Simple ATM ===")
    if not login():
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()