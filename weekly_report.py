import feedparser
from datetime import datetime
import smtplib
import imaplib
import time
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# Email configuration
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')
recipient_email = 'info@mukundan14.co.site'
subject = 'Weekly Entrepreneurial Content'

# SMTP (sending) server details
smtp_server = 'smtp0001.neo.space'
smtp_port = 587

# IMAP (receiving) server details
imap_server = 'imap0001.neo.space'
imap_port = 993

# Function to fetch top 100 entrepreneurial articles from an RSS feed
def fetch_entrepreneurial_articles():
    feed_url = "https://news.ycombinator.com/rss"  # Example RSS feed URL
    feed = feedparser.parse(feed_url)
    articles = []

    # Filter articles published in the current week
    for entry in feed.entries:
        published_time = datetime(*entry.published_parsed[:6])
        if (datetime.now() - published_time).days <= 7:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": published_time.strftime("%Y-%m-%d")
            })
        if len(articles) >= 100:
            break
    
    return articles

def send_email():
    # Fetch articles
    articles = fetch_entrepreneurial_articles()
    body = "<h1>This Week's Top 100 Entrepreneurial Articles</h1><ul>"
    body += "".join(f"<li><a href='{article['link']}'>{article['title']}</a> (Published on: {article['published']})</li>" for article in articles)
    body += "</ul>"

    # Create the message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText(body, 'html', 'utf-8'))

    try:
        # Send the email
        smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
        smtp_obj.starttls()
        smtp_obj.login(sender_email, sender_password)
        smtp_obj.sendmail(sender_email, recipient_email, message.as_string())
        smtp_obj.quit()
        print('Email sent successfully.')

        # Append the sent email to the IMAP server's "Sent" folder
        imap_obj = imaplib.IMAP4_SSL(imap_server, imap_port)
        imap_obj.login(sender_email, sender_password)
        imap_obj.append('Sent', '', imaplib.Time2Internaldate(time.time()), message.as_bytes())
        imap_obj.logout()
        print('Email appended to "Sent" folder.')
    except smtplib.SMTPException as e:
        print('Error sending email:', str(e))
    except imaplib.IMAP4.error as e:
        print('Error appending email to "Sent" folder:', str(e))

# Call the function to send the email and append it to the "Sent" folder
send_email()
