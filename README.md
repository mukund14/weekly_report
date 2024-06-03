# Weekly Report Automation

This repository contains a Python script and a GitHub Actions workflow to automate the sending of weekly emails with the latest entrepreneurial and marketing content. The script fetches the top 100 entrepreneurial articles, recent marketing blog posts, videos, and podcasts from specified sources, and emails them every Saturday at 10:00 AM Pacific Time.

## Features

- **Automated Email Reports**: Sends a weekly email with curated content.
- **Content Sources**:
  - Entrepreneurial articles from Hacker News RSS feed.
  - Marketing articles from HubSpot, Jenna Kutcher, Amy Porterfield, Jasmine Star, Natalie Ellis, Dr. JJ Peterson, Donald Miller, Marie Forleo, and others.
  - Recent podcast episodes from the same sources.
- **Scheduling**: Uses GitHub Actions to run the script every Saturday at 10:00 AM PT.

## Setup

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/mukund14/weekly_report.git
   cd weekly_report
Set Up Environment Variables:
Add your email credentials to GitHub Secrets:

SENDER_EMAIL: Your sender email address.
SENDER_PASSWORD: Your sender email password.
Update Workflow File:
Ensure the .github/workflows/send_weekly_report.yml file is set up correctly.

Run the Script Manually:
You can also run the script manually to test:

```sh
  python weekly_report.py
Files
weekly_report.py: The main script that fetches and sends the email.
.github/workflows/send_weekly_report.yml: GitHub Actions workflow file to schedule the script.
How It Works
Fetches Content: The script fetches the latest articles and podcasts from specified sources published in the past week.
Creates Email: Combines the fetched content into an HTML email format.
Sends Email: Uses SMTP to send the email and IMAP to log the sent email.
Dependencies
feedparser
requests
beautifulsoup4
Install dependencies using:

```sh
pip install -r requirements.txt
