import smtplib
import random

EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"

def send_otp(user_email):
    otp = random.randint(100000, 999999)
    print(f"📩 Sending OTP to {user_email}...")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            message = f"Subject: Your OTP Code\n\nYour OTP code is {otp}. It expires in 5 minutes."
            server.sendmail(EMAIL_ADDRESS, user_email, message)
        
        entered_otp = input("Enter the OTP sent to your email: ")
        return entered_otp == str(otp)
    
    except Exception as e:
        print(f"❌ Email error: {e}")
        return False
