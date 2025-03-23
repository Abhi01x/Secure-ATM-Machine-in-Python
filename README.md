# Secure-ATM-Machine-in-Python

## 🚀 Features
- **User Authentication**: Secure login with hashed PIN.
- **Two-Factor Authentication (2FA)**: OTP verification via email.
- **Balance Inquiry, Deposit, Withdrawal**: Standard ATM operations.
- **Transaction History**: Logs and displays previous transactions.
- **Session Timeout**: Auto logout after inactivity.
- **Admin Mode**: Special admin access to manage user accounts.

## 📂 Project Structure
ATM-Project/ │── atm.py # Main Python script │── otp_verification.py # OTP handling script │── database.json # Stores user data securely │── README.md # Documentation │── requirements.txt # Dependencies

## 🛠️ Setup Instructions
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

2️⃣ Configure Email for OTP
Edit otpverify.py and set up SMTP email credentials:
EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"

3️⃣ Run the ATM Application
python atm.py

```
## 🏗️ Features Breakdown

### 🔐 Secure Login & PIN Hashing
- PINs are stored securely using SHA-256 hashing.
- Prevents brute-force attacks with a limited number of attempts.

### 🔑 Two-Factor Authentication (2FA)
- Sends a One-Time Password (OTP) via email for additional security.
- OTP expires after a short period to prevent reuse.

### 💰 ATM Transactions
- **Balance Inquiry**: Displays current account balance.
- **Deposit Money**: Allows users to deposit money into their account.
- **Withdraw Money**: Ensures sufficient balance before withdrawal.

### 📜 Transaction History
- Stores all user transactions in `database.json`.
- Allows users to review their financial activity.

### ⏳ Session Timeout
- Auto logs out users after a certain period of inactivity.
- Protects against unauthorized access if the user steps away.

### 🛡️ Admin Mode
- Allows admins to add, remove, and manage user accounts.
- Grants elevated permissions to perform maintenance tasks.

### 📌 Future Enhancements
- Biometric authentication support.
- Integration with blockchain for transaction security.
- Mobile app version with QR-based login.

### 👨‍💻 Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.


