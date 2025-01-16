import scrapy

tag = "love"
class QuotesByTagSpider(scrapy.Spider):
    name = 'quotes_by_tag'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [f'http://quotes.toscrape.com/tag/{tag}/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'Etiqueta': tag,
                'Cita': quote.css('span.text::text').get(),
                'Autor': quote.css('span small::text').get()
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
