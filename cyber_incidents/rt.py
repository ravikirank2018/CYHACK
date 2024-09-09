import scrapy
import mysql.connector

class CyberIncidentSpider(scrapy.Spider):
    name = "cyber_incidents"
    start_urls = [
        'https://krebsonsecurity.com/',
        'https://www.cyberscoop.com/category/cybersecurity/',  # Add more URLs as needed
    ]

    def parse(self, response):
        for incident in response.css('article'):
            title = incident.css('h2.entry-title a::text').get()
            date = incident.css('time.entry-date::attr(datetime)').get()
            details = incident.css('div.entry-content p::text').get()

            if title and date and details:
                # Save to MySQL database
                self.save_to_db(title, date, details)

        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def save_to_db(self, title, date, details):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='2004',  # Replace with your MySQL password
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
