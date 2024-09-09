import scrapy

class CyberIncidentSpider(scrapy.Spider):
    name = "cyber_incidents"
    start_urls = ['https://exampleforum.com/incident-reports']

    def parse(self, response):
        for incident in response.css('div.incident'):
            yield {
                'title': incident.css('h2.title::text').get(),
                'date': incident.css('span.date::text').get(),
                'details': incident.css('p.details::text').get(),
            }
        next_page = response.css('a.next_page::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
