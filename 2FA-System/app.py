from flask import Flask, render_template, request
import pyotp
import qrcode
import io
import base64

app = Flask(__name__)

secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        otp = request.form.get("otp")
        result = totp.verify(otp)

    otp_uri = totp.provisioning_uri(
        name="user@example.com",
        issuer_name="2FA System"
    )

    qr = qrcode.make(otp_uri)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render_template(
        "index.html",
        qr=qr_base64,
        secret=secret,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=true)
