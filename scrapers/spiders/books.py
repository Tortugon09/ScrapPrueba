import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            availability_text = book.css('p.instock.availability *::text').getall()
            availability_text = ''.join(availability_text).strip()

            yield {
                'Título': book.css('h3 a::attr(title)').get(),
                'Precio': book.css('div.product_price p.price_color::text').get(),
                'Disponibilidad': availability_text,
            }
            
        next_page = response.css('ul.pager li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
