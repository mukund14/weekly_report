import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email():
    # Email content
    subject = "Weekly Report"
    body = "This is your weekly report."

    # Email details
    from_email = os.getenv('EMAIL')
    to_email = os.getenv('RECIPIENT')
    password = os.getenv('PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')

    print(f"From Email: {from_email}")
    print(f"To Email: {to_email}")

    # Check if environment variables are set correctly
    if not from_email or not to_email or not password:
        print("Environment variables are not set correctly.")
        return

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email()
