import scrapy
import mysql.connector

class CyberIncidentSpider(scrapy.Spider):
    name = "cyber_incidents"
    start_urls = ['https://krebsonsecurity.com/',
        'https://www.cyberscoop.com/category/cybersecurity/',]

    def parse(self, response):
        for incident in response.css('div.incident'):
            title = incident.css('h2.title::text').get()
            date = incident.css('span.date::text').get()
            details = incident.css('p.details::text').get()

            # Save to MySQL database
            self.save_to_db(title, date, details)

            next_page = response.css('a.next_page::attr(href)').get()
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
