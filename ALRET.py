import scrapy
import mysql.connector
import requests
import logging
import os

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

    def __init__(self, *args, **kwargs):
        super(CyberIncidentSpider, self).__init__(*args, **kwargs)
        self.session = requests.Session()
        self.db_config = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', '2004'),
            'database': os.getenv('DB_NAME', 'cyber_incidents_db')
        }
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Log database configuration for debugging (without sensitive info)
        self.logger.debug(f"Database config: {self.db_config}")

    def parse(self, response):
        self.logger.info(f"Parsing URL: {response.url}")
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
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO incidents (title, date, details) VALUES (%s, %s, %s)",
                (title, date, details)
            )
            conn.commit()
            cursor.close()
            conn.close()
            self.logger.info(f"Saved incident to database: {title}")
        except mysql.connector.Error as err:
            self.logger.error(f"Error saving incident to database: {err}")

    def is_attack(self, title, details):
        keywords = ['attack', 'ransomware', 'breach', 'ddos', 'phishing']
        for keyword in keywords:
            if keyword in title.lower() or keyword in details.lower():
                return True
        return False

    def send_alert(self, title, date, details):
        alert_data = {
            'title': title,
            'date': date,
            'details': details
        }
        try:
            response = self.session.post('http://localhost:5000/alert', json=alert_data)
            response.raise_for_status()
            self.logger.info(f"Alert data sent successfully for: {title}")
        except requests.RequestException as e:
            self.logger.error(f"Failed to send alert data: {e}")
