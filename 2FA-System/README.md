# 🔐 2FA System (TOTP Based Authentication)

## Short Description
Multi-factor login system using Time-Based One-Time Passwords (TOTP).

## Brief Description
This project implements a Two-Factor Authentication (2FA) system using TOTP.
A secret key is generated and displayed as a QR code, which can be scanned using
Google Authenticator. The OTP generated is verified on the server side.

## Tools Used
- Python
- Flask
- PyOTP
- Google Authenticator
- QRCode
- Pillow

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Run:
   python app.py
3. Open browser:
   http://127.0.0.1:5000/

## Notes
Ensure system time is synced (NTP) for correct OTP validation.
