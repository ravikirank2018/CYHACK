import scrapy


class CyberIncidentSpiderSpider(scrapy.Spider):
    name = "cyber_incident_spider"
    allowed_domains = ["exampleforum.com"]
    start_urls = ["https://exampleforum.com"]

    def parse(self, response):
        pass
