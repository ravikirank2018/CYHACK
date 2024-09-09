import scrapy
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class CyberIncidentSpider(scrapy.Spider):
    name = "cyber_incidents"
    start_urls = [
        'https://www.cert-in.org.in/',  # CERT-In
        'https://cybersafeindia.org/',  # Cyber Safe India
        'https://thehackernews.com/search/label/India',  # The Hacker News - India
        'https://economictimes.indiatimes.com/tech/internet',  # Economic Times - Internet
        'https://www.indiatoday.in/technology',  # India Today - Technology
        # Add more URLs as needed
    ]

    def parse(self, response):
        for incident in response.css('article'):
            title = incident.css('h2.entry-title a::text').get()
            date = incident.css('time.entry-date::attr(datetime)').get()
            details = incident.css('div.entry-content p::text').get()

            if title and date and details:
                # Check for keywords indicating a cyber attack
                if self.is_attack(title, details):
                    self.send_alert(title, date, details)

                # Save to MySQL database
                self.save_to_db(title, date, details)

        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def save_to_db(self, title, date, details):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2004',
            database='cyber_incidents_db'
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO incidents (title, date, details) VALUES (%s, %s, %s)",
            (title, date, details)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def is_attack(self, title, details):
      
        keywords = ['attack', 'ransomware', 'breach', 'DDoS', 'phishing']
        for keyword in keywords:
            if keyword in title.lower() or keyword in details.lower():
                return True
        return False

    def send_alert(self, title, date, details):
        # Define email sender and receiver
        sender_email = "rkiran@gitam.in"
        receiver_email = "ravikirank2004@gmail.com"
        password = "rAVI2004@"

        # Create the email content
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = f"Alert: Cyber Attack Detected - {title}"

        body = f"Title: {title}\nDate: {date}\nDetails: {details}"
        message.attach(MIMEText(body, "plain"))

        # Connect to the email server and send the email
        try:
            server = smtplib.SMTP('smtp.example.com', 587)  # Update SMTP server and port
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.close()
            print(f"Alert sent successfully for: {title}")
        except Exception as e:
            print(f"Failed to send alert: {e}")
