# 🔐 2FA System (TOTP Based Authentication)

## Short Description
Multi-Factor Login System using Time-Based One-Time Password (TOTP).

## Brief Description
This project includes an implementation of a Two-Factor Authentication system based on TOTP.
A secret key is generated and displayed in the form of a QR code, which is scanned using Google Authenticator,
The OTP is verified on the server side.

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
Sync the time of the system (NTP) for proper OTP verification.
