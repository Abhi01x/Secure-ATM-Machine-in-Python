import json
import time
import hashlib
import otp_verification

DB_FILE = "database.json"

# Load user data from the database
def load_users():
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save user data to the database
def save_users(users):
    with open(DB_FILE, "w") as file:
        json.dump(users, file, indent=4)

# Hash PIN using SHA-256
def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

# User authentication
def authenticate():
    users = load_users()
    card_number = input("Enter your card number: ")
    
    if card_number in users:
        for _ in range(3):  # Allow max 3 attempts
            pin = input("Enter your PIN: ")
            if hash_pin(pin) == users[card_number]["pin"]:
                print("✅ Authentication successful.")
                if otp_verification.send_otp(users[card_number]["email"]):
                    return card_number
                else:
                    print("❌ OTP verification failed.")
                    return None
            else:
                print("❌ Incorrect PIN. Try again.")
        print("⛔ Too many failed attempts. Exiting.")
    else:
        print("❌ Card number not found.")
    
    return None

# Display account balance
def check_balance(card_number):
    users = load_users()
    print(f"💰 Your balance: ${users[card_number]['balance']}")

# Deposit money
def deposit(card_number):
    users = load_users()
    amount = float(input("Enter amount to deposit: "))
    
    if amount > 0:
        users[card_number]["balance"] += amount
        users[card_number]["transactions"].append(f"Deposited: ${amount}")
        save_users(users)
        print("✅ Deposit successful.")
    else:
        print("❌ Invalid amount.")

# Withdraw money
def withdraw(card_number):
    users = load_users()
    amount = float(input("Enter amount to withdraw: "))
    
    if 0 < amount <= users[card_number]["balance"]:
        users[card_number]["balance"] -= amount
        users[card_number]["transactions"].append(f"Withdrawn: ${amount}")
        save_users(users)
        print("✅ Withdrawal successful.")
    else:
        print("❌ Insufficient balance or invalid amount.")

# Show transaction history
def transaction_history(card_number):
    users = load_users()
    print("📜 Transaction History:")
    for transaction in users[card_number]["transactions"]:
        print(transaction)

# ATM menu
def atm_menu(card_number):
    while True:
        print("\n🏦 ATM Menu")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")
        
        choice = input("Select an option: ")
        if choice == "1":
            check_balance(card_number)
        elif choice == "2":
            deposit(card_number)
        elif choice == "3":
            withdraw(card_number)
        elif choice == "4":
            transaction_history(card_number)
        elif choice == "5":
            print("🔒 Logging out...")
            time.sleep(1)
            break
        else:
            print("❌ Invalid option. Try again.")

# Main function
def main():
    print("🏦 Welcome to Secure ATM")
    card_number = authenticate()
    
    if card_number:
        atm_menu(card_number)

if __name__ == "__main__":
    main()
