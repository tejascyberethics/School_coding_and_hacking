import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email credentials
sender_email = "20206473tejas@ambiencepublicschool.com"
sender_password = "your_email_password"
receiver_email = "victim@example.com"

# Create the email content
subject = "Urgent: Account Verification Required"
body = """
Dear User,

We have detected suspicious activity on your account. Please verify your identity by clicking the link below and logging in with your credentials:

<a href="http://your_phishing_site.com">Verify Your Account</a>

If you do not verify your account within 24 hours, your account will be temporarily suspended.

Thank you for your cooperation.

Sincerely,
Security Team
"""

# Create MIME message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'html'))

# Send the email
try:
    server = smtplib.SMTP('smtp.example.com', 587)  # Use appropriate SMTP server and port
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
    print("Phishing email sent successfully.")
except Exception as e:
    print(f"Failed to send phishing email: {e}")